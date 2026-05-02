# app.py — Flask Backend for EduFees Management System (Agentic AI Edition)

from flask import Flask, render_template, request, jsonify, send_file, session
import pandas as pd
import io
import uuid

import excel_handler as eh
from config import *

app = Flask(__name__)
app.secret_key = "edufees-secret-2024"

eh.init_excel()

# ── In-memory agent store (session_id -> Agent) ──────────────────────────────
_agents: dict = {}


# ═══════════════════════════════════════════════════════════════════════════════
#  PAGE ROUTES
# ═══════════════════════════════════════════════════════════════════════════════

@app.route("/")
def dashboard():
    stats = eh.get_dashboard_stats()
    return render_template("dashboard.html", stats=stats, active_page="dashboard")


@app.route("/college")
def college():
    return render_template("college.html", programs=COLLEGE_CLASSES, sections=COLLEGE_SECTIONS,
                           default_fees=DEFAULT_COLLEGE_FEES, active_page="college")


@app.route("/university")
def university():
    return render_template("university.html", departments=DEPARTMENTS,
                           default_fees=DEFAULT_UNI_FEES, max_semesters=MAX_SEMESTERS,
                           active_page="university")


@app.route("/fees")
def fee_management():
    return render_template("fee_management.html", programs=COLLEGE_CLASSES,
                           departments=DEPARTMENTS, max_semesters=MAX_SEMESTERS,
                           active_page="fees")


@app.route("/structures")
def fee_structures():
    college_rows = [{"program": p, "annual_fee": f, "installment": round(f / 4, 2), "installments": 4}
                    for p, f in DEFAULT_COLLEGE_FEES.items()]
    uni_rows = [{"department": d, "semester_fee": f, "installment": round(f / 2, 2),
                 "total_program": f * MAX_SEMESTERS} for d, f in DEFAULT_UNI_FEES.items()]
    return render_template("fee_structures.html", college_rows=college_rows, uni_rows=uni_rows,
                           active_page="structures")


@app.route("/ai-assistant")
def ai_assistant():
    return render_template("ai_assistant.html", active_page="ai")


# ═══════════════════════════════════════════════════════════════════════════════
#  AI AGENT API
# ═══════════════════════════════════════════════════════════════════════════════

@app.route("/api/chat", methods=["POST"])
def api_chat():
    try:
        from agent_config import create_agent, run_agent
    except ImportError as e:
        return jsonify({"success": False, "response": f"Agent module error: {e}"})

    data    = request.json or {}
    message = data.get("message", "").strip()
    api_key = data.get("api_key", "").strip()
    model   = data.get("model", "groq")
    reset   = data.get("reset", False)

    if not message:
        return jsonify({"success": False, "response": "Please enter a message."})

    if "sid" not in session:
        session["sid"] = str(uuid.uuid4())
    sid = session["sid"]

    if reset or sid not in _agents:
        try:
            _agents[sid] = create_agent(model_choice=model, api_key=api_key or None)
        except Exception as e:
            return jsonify({"success": False, "response": f"Could not create agent: {e}"})

    agent    = _agents[sid]
    response = run_agent(agent, message)
    return jsonify({"success": True, "response": response})


@app.route("/api/chat/reset", methods=["POST"])
def api_chat_reset():
    sid = session.get("sid")
    if sid:
        _agents.pop(sid, None)
        session.pop("sid", None)
    return jsonify({"success": True})


# ═══════════════════════════════════════════════════════════════════════════════
#  COLLEGE API
# ═══════════════════════════════════════════════════════════════════════════════

@app.route("/api/college/students")
def api_college_students():
    program = request.args.get("program")
    section = request.args.get("section")
    df = eh.get_college_students(
        program_filter=program if program and program != "All" else None,
        section_filter=section if section and section != "All" else None,
    )
    return jsonify(df.to_dict(orient="records"))


@app.route("/api/college/add", methods=["POST"])
def api_college_add():
    data = request.json
    for f in ["name", "program", "roll_no", "academic_year", "total_fee"]:
        if not data.get(f):
            return jsonify({"success": False, "message": f"Field '{f}' is required."}), 400
    result = eh.add_college_student(
        name=data["name"], father_name=data.get("father_name", ""),
        program=data["program"], section=data.get("section", "A"),
        roll_no=data["roll_no"], academic_year=data["academic_year"],
        total_annual_fee=float(data["total_fee"]),
    )
    return jsonify(result)


@app.route("/api/college/update", methods=["POST"])
def api_college_update():
    data = request.json
    sid  = data.pop("student_id", None)
    if not sid:
        return jsonify({"success": False, "message": "student_id required."}), 400
    return jsonify(eh.update_college_student(sid, **data))


@app.route("/api/college/delete", methods=["POST"])
def api_college_delete():
    sid = request.json.get("student_id")
    if not sid:
        return jsonify({"success": False, "message": "student_id required."}), 400
    return jsonify(eh.delete_college_student(sid))


@app.route("/api/college/approve", methods=["POST"])
def api_college_approve():
    data    = request.json
    sid     = data.get("student_id")
    inst_no = int(data.get("installment_number", 0))
    if not sid or inst_no not in [1, 2, 3, 4]:
        return jsonify({"success": False, "message": "Invalid request."}), 400
    return jsonify(eh.approve_college_installment(sid, inst_no))


@app.route("/api/college/download")
def api_college_download():
    program = request.args.get("program")
    df = eh.get_college_students(program_filter=program if program and program != "All" else None)
    buf = io.BytesIO()
    df.to_csv(buf, index=False)
    buf.seek(0)
    return send_file(buf, mimetype="text/csv", as_attachment=True, download_name="college_students.csv")


# ═══════════════════════════════════════════════════════════════════════════════
#  UNIVERSITY API
# ═══════════════════════════════════════════════════════════════════════════════

@app.route("/api/university/students")
def api_uni_students():
    dept = request.args.get("department")
    df = eh.get_university_students(department_filter=dept if dept and dept != "All" else None)
    return jsonify(df.to_dict(orient="records"))


@app.route("/api/university/fee-records")
def api_uni_fee_records():
    name = request.args.get("name")
    dept = request.args.get("department")
    sem  = request.args.get("semester")
    df = eh.get_university_fee_records(
        name=name if name else None,
        department=dept if dept and dept != "All" else None,
        semester=int(sem) if sem and sem != "All" else None,
    )
    return jsonify(df.to_dict(orient="records"))


@app.route("/api/university/add", methods=["POST"])
def api_uni_add():
    data = request.json
    for f in ["name", "department", "roll_no"]:
        if not data.get(f):
            return jsonify({"success": False, "message": f"Field '{f}' required."}), 400
    result = eh.add_university_student(
        name=data["name"], father_name=data.get("father_name", ""),
        department=data["department"], roll_no=data["roll_no"],
        semester_fee=float(data.get("semester_fee", 0)),
        starting_semester=int(data.get("starting_semester", 1)),
    )
    return jsonify(result)


@app.route("/api/university/update", methods=["POST"])
def api_uni_update():
    data = request.json
    sid  = data.pop("student_id", None)
    if not sid:
        return jsonify({"success": False, "message": "student_id required."}), 400
    return jsonify(eh.update_university_student(sid, **data))


@app.route("/api/university/delete", methods=["POST"])
def api_uni_delete():
    sid = request.json.get("student_id")
    if not sid:
        return jsonify({"success": False, "message": "student_id required."}), 400
    return jsonify(eh.delete_university_student(sid))


@app.route("/api/university/approve", methods=["POST"])
def api_uni_approve():
    data    = request.json
    rec_id  = data.get("record_id")
    inst_no = int(data.get("installment_number", 0))
    if not rec_id or inst_no not in [1, 2]:
        return jsonify({"success": False, "message": "Invalid request."}), 400
    return jsonify(eh.approve_uni_installment(rec_id, inst_no))


@app.route("/api/university/download")
def api_uni_download():
    dept = request.args.get("department")
    df = eh.get_university_fee_records(department=dept if dept and dept != "All" else None)
    buf = io.BytesIO()
    df.to_csv(buf, index=False)
    buf.seek(0)
    return send_file(buf, mimetype="text/csv", as_attachment=True, download_name="university_fees.csv")


# ═══════════════════════════════════════════════════════════════════════════════
#  DASHBOARD API
# ═══════════════════════════════════════════════════════════════════════════════

@app.route("/api/stats")
def api_stats():
    return jsonify(eh.get_dashboard_stats())


if __name__ == "__main__":
    app.run(debug=True, port=5000)