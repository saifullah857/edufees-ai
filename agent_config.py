# agent_config.py — Agno AI Agent (Groq LLaMA 3.3 / Gemini 2.0)

import json
from typing import Optional
from agno.agent import Agent
from agno.models.groq import Groq
from agno.models.google import Gemini

import excel_handler as eh
from config import (
    COLLEGE_CLASSES, DEPARTMENTS, DEFAULT_COLLEGE_FEES,
    DEFAULT_UNI_FEES, MAX_SEMESTERS,
)


# ═══════════════════════════════════════════════════════════════════════════════
#  TOOL FUNCTIONS  (each returns a JSON string for the LLM)
# ═══════════════════════════════════════════════════════════════════════════════

def search_university_student(
    name:       Optional[str] = None,
    department: Optional[str] = None,
    semester:   Optional[int] = None,
) -> str:
    """
    Search university students by name, department, and/or semester.
    Returns fee records including installment status.
    Pass semester as an integer (1-8) or leave null if unknown.
    """
    try:
        semester = None if semester in ("", None) else int(semester)
    except Exception:
        semester = None

    df = eh.get_university_fee_records(
        name=name, department=department, semester=semester
    )
    if df.empty:
        return json.dumps({"found": False, "message": "No students found with the given criteria."})
    return json.dumps({"found": True, "count": len(df), "records": df.to_dict(orient="records")}, default=str)


def search_college_student(
    name:    Optional[str] = None,
    program: Optional[str] = None,
    section: Optional[str] = None,
) -> str:
    """
    Search college students by name, program (FA/ICS/ICOM/FSC Medical/FSC Engineering/IT),
    and/or section (A/B/C/D/E).
    """
    df = eh.get_college_students(
        program_filter=program if program else None,
        section_filter=section if section else None,
    )
    if name:
        df = df[df["Name"].str.lower().str.contains(name.lower(), na=False)]
    if df.empty:
        return json.dumps({"found": False, "message": "No college students found."})
    return json.dumps({"found": True, "count": len(df), "records": df.to_dict(orient="records")}, default=str)


def get_college_fee_status(student_id: str) -> str:
    """Get full fee status for a college student by their Student_ID (e.g. COL-12345678)."""
    df  = eh.get_college_students()
    row = df[df["Student_ID"] == student_id]
    if row.empty:
        return json.dumps({"found": False, "message": f"No college student found with ID {student_id}"})
    return json.dumps({"found": True, "data": row.iloc[0].to_dict()}, default=str)


def get_university_fee_status(student_id: str) -> str:
    """Get all semester fee records for a university student by their Student_ID."""
    df = eh.get_university_fee_records(student_id=student_id)
    if df.empty:
        return json.dumps({"found": False, "message": f"No fee records found for {student_id}"})
    return json.dumps({"found": True, "records": df.to_dict(orient="records")}, default=str)


def approve_college_fee(student_id: str, installment_number: int) -> str:
    """
    Approve a specific installment for a college student.
    installment_number must be 1, 2, 3, or 4.
    """
    result = eh.approve_college_installment(student_id, installment_number)
    return json.dumps(result)


def approve_university_fee(record_id: str, installment_number: int) -> str:
    """
    Approve a specific installment for a university fee record.
    record_id is the UFR-XXXXXXXX id from fee records.
    installment_number must be 1 or 2.
    When both are approved, the system auto-creates the next semester record.
    """
    result = eh.approve_uni_installment(record_id, installment_number)
    return json.dumps(result)


def list_all_college_students(program: Optional[str] = None) -> str:
    """
    List college students, optionally filtered by program.
    program values: FA, ICS, ICOM, FSC Medical, FSC Engineering, IT
    """
    df = eh.get_college_students(program_filter=program)
    if df.empty:
        return json.dumps({"found": False, "message": "No college students found."})
    return json.dumps({"count": len(df), "students": df.to_dict(orient="records")}, default=str)


def list_all_university_students(department: Optional[str] = None) -> str:
    """
    List university students, optionally filtered by department.
    """
    df = eh.get_university_students(department_filter=department)
    if df.empty:
        return json.dumps({"found": False, "message": "No university students found."})
    return json.dumps({"count": len(df), "students": df.to_dict(orient="records")}, default=str)


def get_system_summary() -> str:
    """Get a high-level dashboard summary: total students, fees cleared, pending records, breakdowns."""
    stats = eh.get_dashboard_stats()
    return json.dumps(stats)


def get_default_fees() -> str:
    """Return the default fee structures for all college programs and university departments."""
    return json.dumps({
        "college_fees_per_program": DEFAULT_COLLEGE_FEES,
        "university_fees_per_semester_per_department": DEFAULT_UNI_FEES,
        "note": f"University has {MAX_SEMESTERS} semesters, 2 installments each. College has 4 installments per year.",
    })


# ═══════════════════════════════════════════════════════════════════════════════
#  SYSTEM PROMPT
# ═══════════════════════════════════════════════════════════════════════════════

SYSTEM_PROMPT = f"""You are **EduFees AI**, a smart, friendly, and highly capable Fees Management Assistant
for an educational institution that has both a College and a University.

---

## INSTITUTION OVERVIEW

**College Programs:** {", ".join(COLLEGE_CLASSES)}
- 4 installments per academic year
- Each program has its own annual fee structure
- Students can be in Section A, B, C, D, or E

**University Departments:** {", ".join(DEPARTMENTS)}
- 8 semesters total per student
- 2 installments per semester
- When both installments of a semester are approved → next semester auto-creates
- Students can start from any semester (1–8)

---

## YOUR CAPABILITIES

You have access to these tools:
1. **search_university_student** – find uni students by name, department, semester
2. **search_college_student** – find college students by name, program, section
3. **get_college_fee_status** – full fee details for one college student
4. **get_university_fee_status** – all semester records for one uni student
5. **approve_college_fee** – mark a college installment as Approved
6. **approve_university_fee** – mark a university installment as Approved
7. **list_all_college_students** – list all (or filtered) college students
8. **list_all_university_students** – list all (or filtered) university students
9. **get_system_summary** – dashboard stats (totals, breakdowns, pending counts)
10. **get_default_fees** – default fee structures for all programs/departments

---

## IMPORTANT RULES

- Always pass `semester` as an INTEGER (e.g., 1, 2, 3). Never pass "" for numeric fields — use null.
- For `program` in college: use exact values: FA, ICS, ICOM, FSC Medical, FSC Engineering, IT
- For `installment_number` in college: must be 1, 2, 3, or 4
- For `installment_number` in university: must be 1 or 2
- `record_id` for university is the UFR-XXXXXXXX field, NOT the student_id
- When approving fees, always confirm what was approved and show the updated status

---

## RESPONSE STYLE

- Be warm, professional, and clear — like a helpful admin colleague
- Format responses with markdown: use **bold**, tables, bullet lists where helpful
- For student lists, use well-formatted markdown tables with all relevant columns
- When showing fees, always include Rs. prefix and use comma formatting
- Proactively suggest next steps (e.g., "Would you like me to approve the next installment?")
- If a student has pending fees, highlight them clearly
- When you successfully approve something, celebrate it briefly 🎉
- If you can't find a student, suggest alternative search strategies

---

## EXAMPLE INTERACTIONS

- "Show pending fees" → call get_system_summary, then list_all_college_students + get_university_fee_records filtered to pending
- "Approve install 2 for COL-12345" → call approve_college_fee with correct args, then report result
- "Which CS students are in semester 3?" → call search_university_student with department="Computer Science", semester=3
- "How much does FSC Medical cost?" → call get_default_fees and extract that program's info
"""


# ═══════════════════════════════════════════════════════════════════════════════
#  AGENT FACTORY
# ═══════════════════════════════════════════════════════════════════════════════

def create_agent(model_choice: str = "groq", api_key: str = "") -> Agent:
    """Create and return a new Agno Agent with all fee management tools."""
    tools = [
        search_university_student,
        search_college_student,
        get_college_fee_status,
        get_university_fee_status,
        approve_college_fee,
        approve_university_fee,
        list_all_college_students,
        list_all_university_students,
        get_system_summary,
        get_default_fees,
    ]

    if model_choice == "gemini":
        model = Gemini(id="gemini-2.0-flash", api_key=api_key if api_key else None)
    else:
        model = Groq(id="llama-3.3-70b-versatile", api_key=api_key if api_key else None)

    return Agent(
        model=model,
        tools=tools,
        instructions=[SYSTEM_PROMPT],
        markdown=True,
        
    )


def run_agent(agent: Agent, user_message: str) -> str:
    """Run the agent with a user message and return the text response."""
    try:
        user_message = user_message.replace('""', "null")
        response     = agent.run(user_message)
        if hasattr(response, "content"):
            return response.content
        return str(response)
    except Exception as e:
        error = str(e)
        if "api_key" in error.lower() or "authentication" in error.lower() or "401" in error:
            return "❌ **Invalid or missing API key.** Please check your Groq/Gemini API key at the top of the page and try again."
        if "rate_limit" in error.lower() or "429" in error:
            return "⏳ **Rate limit reached.** Please wait a moment and try again."
        return f"❌ **Agent error:** {error}"