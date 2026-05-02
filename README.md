<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=220&section=header&text=EduFees%20AI&fontSize=80&fontColor=fff&animation=twinkling&fontAlignY=38&desc=🎓%20AI-Powered%20College%20%26%20University%20Fees%20Management&descAlignY=62&descSize=20&descColor=fff" width="100%"/>

<!-- Typing Animation -->
<a href="https://github.com/saifullah857/edufees-ai">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=22&pause=1000&color=6C63FF&center=true&vCenter=true&multiline=true&width=700&height=60&lines=Manage+Student+Fees+with+AI+🤖;Natural+Language+%7C+Excel+%7C+Flask+%7C+Agno" alt="Typing SVG" />
</a>

<br/>

<!-- Badge Row 1 - Tech Stack -->
<p>
  <img src="https://img.shields.io/badge/Python-3.10%2B-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
  <img src="https://img.shields.io/badge/Flask-3.0%2B-000000?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/Agno-AI%20Agent%20Framework-6C63FF?style=for-the-badge&logo=openai&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-2.1%2B-150458?style=for-the-badge&logo=pandas&logoColor=white" />
</p>

<!-- Badge Row 2 - AI Models -->
<p>
  <img src="https://img.shields.io/badge/Groq-LLaMA%203.3%2070B-F55036?style=for-the-badge&logo=meta&logoColor=white" />
  <img src="https://img.shields.io/badge/Gemini-2.0%20Flash-4285F4?style=for-the-badge&logo=google&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenPyXL-Excel%20Engine-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge&logo=opensourceinitiative&logoColor=white" />
</p>

<!-- Badge Row 3 - Social (fixed with correct username) -->
<p>
  <img src="https://img.shields.io/github/stars/saifullah857/edufees-ai?style=for-the-badge&logo=github&color=yellow&labelColor=black" />
  <img src="https://img.shields.io/github/forks/saifullah857/edufees-ai?style=for-the-badge&logo=github&color=blue&labelColor=black" />
  <img src="https://img.shields.io/github/issues/saifullah857/edufees-ai?style=for-the-badge&logo=github&color=red&labelColor=black" />
  <img src="https://img.shields.io/github/last-commit/saifullah857/edufees-ai?style=for-the-badge&logo=git&color=orange&labelColor=black" />
</p>

<br/>

<blockquote>
<b>EduFees AI</b> is a full-stack, AI-powered fees management platform for educational institutions —<br/>
combining a clean <b>Flask</b> web UI, live <b>Excel</b> persistence, and a conversational <b>AI Agent</b><br/>
powered by <b>Groq LLaMA 3.3</b> or <b>Gemini 2.0</b> that can search, report, and approve fees through natural language.
</blockquote>

<br/>

[![⭐ Star this repo if it helped you!](https://img.shields.io/badge/⭐%20Star%20this%20repo%20if%20it%20helped%20you!-yellow?style=for-the-badge)](https://github.com/saifullah857/edufees-ai)

</div>

---

## 📸 Preview

<div align="center">

| Dashboard | AI Chat | Fee Management |
|:---:|:---:|:---:|
| 📊 Live Stats | 🤖 Natural Language | ✅ Approve Installments |
| College + University | Groq / Gemini | Excel Auto-Updated |

> _Screenshots coming soon — run the app locally to see it in action!_

</div>

---

## 🌟 Why EduFees AI?

<div align="center">

```
 Traditional Fee Management          EduFees AI
 ─────────────────────────    vs    ────────────────────────────
  Manual Excel sheets         →     Auto-formatted Excel + AI
  Phone calls to check fees   →     "Show me Ali's fee status"
  Paper records               →     Digital with instant search
  Missed installments         →     Highlighted pending alerts
  No approvals workflow       →     One-click or chat approval
```

</div>

---

## ✨ Feature Highlights

<div align="center">

| 🏫 College | 🏛️ University | 🤖 AI Agent | 📊 Data |
|:---:|:---:|:---:|:---:|
| 4 Installments/Year | 8 Semesters × 2 Inst. | Natural Language Chat | Live Excel Sync |
| Sections A–E | Auto Semester Unlock | Approve via Chat | Color-coded Sheets |
| 6 Programs | 15 Departments | Groq + Gemini Models | CSV Export |
| Custom Fee Tiers | Full Fee History | 10 Powerful Tools | 3-Sheet Workbook |

</div>

---

## 🏗️ System Architecture

```
╔══════════════════════════════════════════════════════════════════╗
║                        EduFees AI System                        ║
╠══════════════╦═══════════════════════╦══════════════════════════╣
║   Flask UI   ║    Agno AI Agent      ║     Excel Data Store     ║
║  ──────────  ║  ─────────────────    ║  ──────────────────────  ║
║  /dashboard  ║  LLaMA 3.3 70B (Groq) ║  College_Students        ║
║  /college    ║  Gemini 2.0 (Google)  ║  University_Students     ║
║  /university ║  10 Tool Functions    ║  University_Fee_Records  ║
║  /fees       ║  Session Memory       ║                          ║
║  /ai-chat    ║                       ║  fees_system.xlsx        ║
╠══════════════╩═══════════════════════╩══════════════════════════╣
║                     excel_handler.py                            ║
║         CRUD • Formatting • Business Logic • Dashboard          ║
╠══════════════════════════════════════════════════════════════════╣
║                        config.py                                ║
║      Constants • Fees • Departments • Colors • Statuses         ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## 📁 Project Structure

```
edufees-ai/
│
├── 🐍 app.py                 ← Flask backend — all routes & REST API
├── 🤖 agent_config.py        ← Agno AI Agent (Groq/Gemini) + 10 tools
├── 📊 excel_handler.py       ← Excel CRUD, styling, business logic
├── ⚙️  config.py              ← All constants: fees, depts, colors
├── 📋 requirements.txt       ← pip dependencies
├── 📗 fees_system.xlsx       ← Auto-generated on first run
│
├── 📂 templates/
│   ├── dashboard.html        ← Overview: totals, charts, alerts
│   ├── college.html          ← College student CRUD + fee view
│   ├── university.html       ← University student CRUD + semesters
│   ├── fee_management.html   ← Approve/view all installments
│   ├── fee_structures.html   ← Program & department fee tables
│   └── ai_assistant.html     ← Full-screen AI chat interface
│
└── 📂 static/                ← CSS, JS, icons, assets
```

---

## 🚀 Getting Started

### Prerequisites

```bash
Python 3.10+  |  pip  |  A free Groq or Gemini API key
```

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/saifullah857/edufees-ai.git
cd edufees-ai
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Get a Free API Key

<div align="center">

| Provider | Get Key | Speed | Free Tier |
|:---:|:---:|:---:|:---:|
| **Groq** ⚡ (Recommended) | [console.groq.com](https://console.groq.com) | Ultra-fast | ✅ Yes |
| **Gemini** 🌟 | [aistudio.google.com](https://aistudio.google.com) | Fast | ✅ Yes |

</div>

### 4️⃣ Run the App

```bash
python app.py
```

> 🌐 Open **http://localhost:5000** in your browser

> 📗 `fees_system.xlsx` is **auto-created** on first run — zero setup needed!

---

## 🤖 AI Agent in Action

The AI understands plain English. Just type naturally:

```
💬 You:  "Show me all Computer Science students in semester 3"
🤖 Bot:  [searches, returns formatted table with fee status]

💬 You:  "Approve installment 2 for record UFR-00001234"
🤖 Bot:  ✅ Installment 2 approved! Semester 4 record auto-created.

💬 You:  "How many students have pending fees right now?"
🤖 Bot:  📊 Here's your dashboard: 42 pending, 88 approved...

💬 You:  "List all FSC Medical students in Section B"
🤖 Bot:  [formatted markdown table with all details]

💬 You:  "What is the fee structure for Biochemistry?"
🤖 Bot:  Rs. 16,000/semester × 8 = Rs. 1,28,000 total
```

### 🛠️ Agent Tools (10 Total)

| # | Function | What It Does |
|:---:|:---|:---|
| 1 | `search_university_student` | Find uni students by name / dept / semester |
| 2 | `search_college_student` | Find college students by name / program / section |
| 3 | `get_college_fee_status` | Full installment breakdown by Student ID |
| 4 | `get_university_fee_status` | All semester records for a university student |
| 5 | `approve_college_fee` | ✅ Mark college installment (1–4) as Approved |
| 6 | `approve_university_fee` | ✅ Mark university installment (1–2) as Approved |
| 7 | `list_all_college_students` | Paginated + filtered college listing |
| 8 | `list_all_university_students` | Paginated + filtered university listing |
| 9 | `get_system_summary` | Live dashboard: totals, breakdowns, pending counts |
| 10 | `get_default_fees` | Fee structures for all programs and departments |

---

## 🎓 College Section

```
Annual Fee  ─────────────────────────────────────────────▶  Year End
    │
    ├── Installment 1  ──▶  🟡 Pending  ──▶  ✅ Approved
    ├── Installment 2  ──▶  🟡 Pending  ──▶  ✅ Approved
    ├── Installment 3  ──▶  🟡 Pending  ──▶  ✅ Approved
    └── Installment 4  ──▶  🟡 Pending  ──▶  ✅ Approved  ──▶  🎓 Year Complete
```

### Programs & Fee Structure

<div align="center">

| Program | Annual Fee | Per Installment | Sections |
|:---:|:---:|:---:|:---:|
| 🎨 FA | Rs. 15,000 | Rs. 3,750 | A–E |
| 💻 ICS | Rs. 18,000 | Rs. 4,500 | A–E |
| 📈 ICOM | Rs. 16,000 | Rs. 4,000 | A–E |
| 🔬 FSC Medical | Rs. 25,000 | Rs. 6,250 | A–E |
| ⚙️ FSC Engineering | Rs. 25,000 | Rs. 6,250 | A–E |
| 🖥️ IT | Rs. 20,000 | Rs. 5,000 | A–E |

</div>

---

## 🏛️ University Section

```
Student Joins Semester N  ──────────────────────────────▶  Graduation
    │
    ├── Semester 1  ──▶  [Inst 1 ✅] + [Inst 2 ✅]  ──▶  Auto-unlock Semester 2
    ├── Semester 2  ──▶  [Inst 1 ✅] + [Inst 2 ✅]  ──▶  Auto-unlock Semester 3
    ├── ...
    └── Semester 8  ──▶  [Inst 1 ✅] + [Inst 2 ✅]  ──▶  🎓 Program Complete
```

### Departments & Semester Fees

<div align="center">

| Department | Per Semester | Total (8 Sem) |
|:---|:---:|:---:|
| 💻 Computer Science | Rs. 18,000 | Rs. 1,44,000 |
| 🧬 Biochemistry | Rs. 16,000 | Rs. 1,28,000 |
| 📊 Business Administration | Rs. 14,000 | Rs. 1,12,000 |
| ⚗️ Physics / Chemistry | Rs. 13,000 | Rs. 1,04,000 |
| 🧠 Psychology / Botany / Zoology | Rs. 11,000 | Rs. 88,000 |
| 📐 Mathematics / Economics | Rs. 10,000 | Rs. 80,000 |
| 📚 Education | Rs. 9,500 | Rs. 76,000 |
| 📜 History | Rs. 9,000 | Rs. 72,000 |
| 🗣️ English / Urdu / Islamiat | Rs. 8,000 | Rs. 64,000 |

</div>

---

## 📊 Excel Data Store

<div align="center">

| Sheet | Purpose | Header Color |
|:---|:---|:---:|
| `College_Students` | Student info + 4 installment columns | 🔵 `#1F4E79` Dark Blue |
| `University_Students` | Basic university student records | 🟢 `#375623` Dark Green |
| `University_Fee_Records` | Per-semester records with 2 installments | 🔴 `#7B2C2C` Dark Red |

### Cell Color Legend

| Color | Hex | Meaning |
|:---:|:---:|:---|
| 🟢 | `#C6EFCE` | Installment **Approved** |
| 🟡 | `#FFEB9C` | Installment **Pending** |
| 🔵 | `#BDD7EE` | Semester **Complete** |
| ⬜ | `#F2F2F2` | Alternate row shading |

</div>

---

## 🌐 Web Routes & REST API

### Pages

| Route | Page | Description |
|:---:|:---:|:---|
| `GET /` | Dashboard | Live stats, totals, quick overview |
| `GET /college` | College | Student CRUD, fee status, filtering |
| `GET /university` | University | Student & semester management |
| `GET /fees` | Fee Management | Approve installments, search records |
| `GET /structures` | Fee Structures | Default fee tables for all programs |
| `GET /ai-assistant` | AI Chat | Full conversational AI interface |

### REST API Reference

```http
# ── AI Agent ────────────────────────────────────────────────────
POST   /api/chat                   → Send message, get AI response
POST   /api/chat/reset             → Clear agent conversation session

# ── College ─────────────────────────────────────────────────────
GET    /api/college/students       → List (filterable by program/section)
POST   /api/college/add            → Add new college student
POST   /api/college/update         → Update student record
POST   /api/college/delete         → Remove student
POST   /api/college/approve        → Approve installment {1,2,3,4}
GET    /api/college/download       → Export to CSV

# ── University ──────────────────────────────────────────────────
GET    /api/university/students    → List (filterable by department)
GET    /api/university/fee-records → Fee records (filter: name/dept/sem)
POST   /api/university/add         → Add new university student
POST   /api/university/update      → Update student
POST   /api/university/delete      → Remove student
POST   /api/university/approve     → Approve installment {1,2}
GET    /api/university/download    → Export to CSV

# ── Dashboard ───────────────────────────────────────────────────
GET    /api/stats                  → Live system-wide statistics
```

---

## ⚙️ Configuration

All constants live in `config.py` — edit once, applied everywhere:

```python
# ── Semesters & Installments ────────────────────────────────────
MAX_SEMESTERS        = 8    # University total semesters
UNI_INSTALLMENTS     = 2    # Installments per university semester
COLLEGE_INSTALLMENTS = 4    # Installments per college year

# ── Fee Statuses ────────────────────────────────────────────────
STATUS_PENDING  = "Pending"
STATUS_APPROVED = "Approved"

# ── Excel Sheet Names ───────────────────────────────────────────
SHEET_COLLEGE = "College_Students"
SHEET_UNI     = "University_Students"
SHEET_UNI_FEE = "University_Fee_Records"

# ── Add / edit departments and programs here ─────────────────────
DEPARTMENTS    = ["Computer Science", "Mathematics", "Physics", ...]
COLLEGE_CLASSES = ["FA", "ICS", "ICOM", "FSC Medical", ...]
```

---

## 📦 Dependencies

```txt
flask>=3.0.0               # Web framework & REST API server
pandas>=2.1.0              # DataFrame operations & filtering
openpyxl>=3.1.0            # Excel read/write with color styling
agno>=1.0.0                # Multi-model AI agent framework
groq>=0.9.0                # Groq API (LLaMA 3.3 70B)
google-generativeai>=0.7.0 # Google Gemini API (2.0 Flash)
```

---

## 🤝 Contributing

Contributions make this project better — all PRs are welcome!

```bash
# 1. Fork the repo on GitHub
# 2. Create your feature branch
git checkout -b feature/your-amazing-feature

# 3. Commit with a clear message
git commit -m "✨ Add: your amazing feature"

# 4. Push to your fork
git push origin feature/your-amazing-feature

# 5. Open a Pull Request 🚀
```

**Ideas for contributions:**
- 📧 Email notifications for overdue installments
- 📱 Mobile-responsive UI improvements
- 📈 Charts & analytics on the dashboard
- 🌙 Dark / light mode toggle
- 🔐 Admin login & role-based access

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

```
MIT License © 2025 saifullah857
Permission is granted to use, copy, modify, and distribute this software freely.
```

---

## 🙏 Acknowledgements

| Tool | Role |
|:---|:---|
| [Agno](https://github.com/agno-agi/agno) | AI Agent framework powering the chat |
| [Groq](https://groq.com) | Ultra-fast LLaMA 3.3 70B inference |
| [Google Gemini](https://aistudio.google.com) | Alternative AI model backend |
| [OpenPyXL](https://openpyxl.readthedocs.io) | Excel formatting & color styling |
| [Flask](https://flask.palletsprojects.com) | Lightweight Python web framework |
| [Shields.io](https://shields.io) | Dynamic badges |
| [Capsule Render](https://github.com/kyechan99/capsule-render) | Animated header & footer |
| [Readme Typing SVG](https://github.com/DenverCoder1/readme-typing-svg) | Animated typing headline |

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=130&section=footer&animation=twinkling" width="100%"/>

### If EduFees AI saved you time, please give it a ⭐ — it means the world!

<a href="https://github.com/saifullah857/edufees-ai">
  <img src="https://img.shields.io/badge/⭐%20Star%20on%20GitHub-black?style=for-the-badge&logo=github" />
</a>
&nbsp;
<a href="https://github.com/saifullah857/edufees-ai/fork">
  <img src="https://img.shields.io/badge/🍴%20Fork%20this%20Repo-grey?style=for-the-badge&logo=github" />
</a>
&nbsp;
<a href="https://github.com/saifullah857/edufees-ai/issues">
  <img src="https://img.shields.io/badge/🐛%20Report%20a%20Bug-red?style=for-the-badge&logo=github" />
</a>

<br/><br/>

*Built with ❤️ for educational institutions · Powered by AI · Open Source*

</div>