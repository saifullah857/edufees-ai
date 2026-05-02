<div align="center">

<!-- Animated Header -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1F4E79,50:375623,100:7B2C2C&height=200&section=header&text=EduFees%20AI&fontSize=70&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Intelligent%20College%20%26%20University%20Fees%20Management&descAlignY=58&descSize=18" width="100%"/>

<!-- Badges Row 1 -->
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0%2B-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Agno](https://img.shields.io/badge/Agno-AI%20Framework-6C63FF?style=for-the-badge&logo=openai&logoColor=white)](https://github.com/agno-agi/agno)
[![Pandas](https://img.shields.io/badge/Pandas-2.1%2B-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)

<!-- Badges Row 2 -->
[![Groq](https://img.shields.io/badge/Groq-LLaMA%203.3%2070B-F55036?style=for-the-badge&logo=meta&logoColor=white)](https://groq.com)
[![Gemini](https://img.shields.io/badge/Gemini-2.0%20Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://aistudio.google.com)
[![OpenPyXL](https://img.shields.io/badge/OpenPyXL-3.1%2B-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)](https://openpyxl.readthedocs.io)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)

<br/>

> **EduFees AI** is a full-stack, AI-powered fees management platform for educational institutions — combining a clean Flask web UI, live Excel data persistence, and a conversational AI agent capable of searching, reporting, and approving student fee installments through natural language.

<br/>

[![Stars](https://img.shields.io/github/stars/yourusername/edufees-ai?style=social)](https://github.com/yourusername/edufees-ai)
[![Forks](https://img.shields.io/github/forks/yourusername/edufees-ai?style=social)](https://github.com/yourusername/edufees-ai)
[![Issues](https://img.shields.io/github/issues/yourusername/edufees-ai?color=red&style=flat-square)](https://github.com/yourusername/edufees-ai/issues)

</div>

---

## 📌 Repository Name & Description

| Field | Value |
|---|---|
| **Repo Name** | `edufees-ai` |
| **Tagline** | *AI-powered College & University Fees Management System with Agno, Groq LLaMA 3.3, Gemini 2.0, Flask & Excel* |
| **Topics** | `flask` `ai-agent` `agno` `groq` `gemini` `fees-management` `excel` `education` `python` `llm` |

---

## ✨ Feature Highlights

<div align="center">

| 🏫 College Management | 🏛️ University Management | 🤖 AI Assistant |
|:---:|:---:|:---:|
| 4 Installments/Year | 8 Semesters × 2 Installments | Natural Language Queries |
| Section A–E Support | Auto Semester Progression | Approve Fees via Chat |
| Program-wise Fee Tiers | Department-wise Tracking | System Reports & Summaries |
| CSV Export | CSV Export | Multi-model (Groq / Gemini) |

</div>

---

## 🖼️ System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                     EduFees AI                          │
│                                                         │
│   ┌──────────┐    ┌───────────────┐    ┌─────────────┐ │
│   │  Flask   │───▶│ excel_handler │───▶│  fees_      │ │
│   │  Web UI  │    │  (CRUD + fmt) │    │  system     │ │
│   └──────────┘    └───────────────┘    │  .xlsx      │ │
│        │                               └─────────────┘ │
│        │          ┌───────────────┐                     │
│        └─────────▶│ agent_config  │                     │
│                   │  Agno Agent   │                     │
│                   └──────┬────────┘                     │
│                          │                              │
│            ┌─────────────┼─────────────┐                │
│            ▼             ▼             ▼                │
│      ┌──────────┐  ┌──────────┐  ┌──────────┐          │
│      │  Groq    │  │  Gemini  │  │  10 Tool │          │
│      │ LLaMA3.3 │  │ 2.0Flash │  │Functions │          │
│      └──────────┘  └──────────┘  └──────────┘          │
└─────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
edufees-ai/
│
├── 📄 app.py                ← Flask backend (routes + API endpoints)
├── 🤖 agent_config.py       ← Agno AI Agent (Groq / Gemini) + 10 tool functions
├── 📊 excel_handler.py      ← Excel CRUD, formatting & business logic
├── ⚙️  config.py             ← Constants: departments, fees, statuses, colors
├── 📋 requirements.txt      ← Python dependencies
├── 📗 fees_system.xlsx      ← Auto-generated data store (3 sheets)
│
├── templates/
│   ├── dashboard.html       ← Overview stats
│   ├── college.html         ← College student management
│   ├── university.html      ← University student management
│   ├── fee_management.html  ← Fee approval UI
│   ├── fee_structures.html  ← Default fee tables
│   └── ai_assistant.html    ← Chat interface
│
└── static/                  ← CSS, JS, assets
```

---

## 🚀 Quick Start

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/edufees-ai.git
cd edufees-ai
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Get API Keys

| Provider | Link | Tier |
|---|---|---|
| **Groq** (LLaMA 3.3 70B) | [console.groq.com](https://console.groq.com) | ✅ Free |
| **Gemini** (2.0 Flash) | [aistudio.google.com](https://aistudio.google.com) | ✅ Free |

### 4️⃣ Run the Application

```bash
python app.py
```

> Open your browser at **http://localhost:5000** 🎉

The `fees_system.xlsx` file is **auto-created** on first run — no setup needed.

---

## 🎓 College Section

```
Annual Fee → Split into 4 Equal Installments
────────────────────────────────────────────
Installment 1 ──▶ Pending / Approved
Installment 2 ──▶ Pending / Approved
Installment 3 ──▶ Pending / Approved
Installment 4 ──▶ Pending / Approved ──▶ 🎓 Year Complete
```

### College Programs & Default Fees

| Program | Annual Fee | Per Installment |
|---|---|---|
| FA | Rs. 15,000 | Rs. 3,750 |
| ICS | Rs. 18,000 | Rs. 4,500 |
| ICOM | Rs. 16,000 | Rs. 4,000 |
| FSC Medical | Rs. 25,000 | Rs. 6,250 |
| FSC Engineering | Rs. 25,000 | Rs. 6,250 |
| IT | Rs. 20,000 | Rs. 5,000 |

---

## 🏛️ University Section

```
8 Semesters × 2 Installments Each
──────────────────────────────────────────────────────────
Semester 1 → Inst 1 + Inst 2 ──▶ ✅ Auto-creates Semester 2
Semester 2 → Inst 1 + Inst 2 ──▶ ✅ Auto-creates Semester 3
...
Semester 8 → Inst 1 + Inst 2 ──▶ 🎓 Program Complete
```

### University Departments & Semester Fees

| Department | Semester Fee | Total Program |
|---|---|---|
| Computer Science | Rs. 18,000 | Rs. 1,44,000 |
| Biochemistry | Rs. 16,000 | Rs. 1,28,000 |
| Business Administration | Rs. 14,000 | Rs. 1,12,000 |
| Physics / Chemistry | Rs. 13,000 | Rs. 1,04,000 |
| Psychology / Botany / Zoology | Rs. 11,000 | Rs. 88,000 |
| Mathematics / Economics | Rs. 10,000 | Rs. 80,000 |
| Education | Rs. 9,500 | Rs. 76,000 |
| History | Rs. 9,000 | Rs. 72,000 |
| English / Urdu / Islamiat | Rs. 8,000 | Rs. 64,000 |

---

## 🤖 AI Assistant Capabilities

The built-in **EduFees AI** agent understands natural language and has access to **10 tool functions**:

```
💬 "Show me pending fees for Computer Science semester 3"
💬 "Approve installment 2 for COL-12345678"
💬 "How many students have cleared all fees this month?"
💬 "List all FSC Medical students in Section B"
💬 "What's the fee structure for Biochemistry?"
💬 "Give me a dashboard summary"
```

### Agent Tools

| # | Tool | Description |
|---|---|---|
| 1 | `search_university_student` | Find uni students by name, dept, semester |
| 2 | `search_college_student` | Find college students by name, program, section |
| 3 | `get_college_fee_status` | Full fee breakdown by Student ID |
| 4 | `get_university_fee_status` | All semester records for a uni student |
| 5 | `approve_college_fee` | Mark a college installment as Approved |
| 6 | `approve_university_fee` | Mark a university installment as Approved |
| 7 | `list_all_college_students` | Filtered college student listing |
| 8 | `list_all_university_students` | Filtered university student listing |
| 9 | `get_system_summary` | Dashboard stats & breakdowns |
| 10 | `get_default_fees` | Default fee structures for all programs |

---

## 📊 Excel Data Store

The `fees_system.xlsx` file contains **3 auto-formatted sheets**:

| Sheet | Contents | Color |
|---|---|---|
| `College_Students` | Student info + 4 installment status columns | 🔵 Dark Blue header |
| `University_Students` | Basic university student records | 🟢 Dark Green header |
| `University_Fee_Records` | Semester-wise records with 2 installments each | 🔴 Dark Red header |

### Color Coding (Cells)

| Color | Meaning |
|---|---|
| 🟢 Light Green | Installment Approved |
| 🟡 Light Yellow | Installment Pending |
| 🔵 Light Blue | Semester Fully Complete |
| ⬜ Light Grey | Alternate row shading |

---

## 🌐 Web Routes

| Route | Page |
|---|---|
| `GET /` | Dashboard with live stats |
| `GET /college` | College student management |
| `GET /university` | University student management |
| `GET /fees` | Fee approval interface |
| `GET /structures` | Default fee structure tables |
| `GET /ai-assistant` | AI chat interface |

### REST API Endpoints

```
POST /api/chat                    ← Send message to AI agent
POST /api/chat/reset              ← Clear agent session

GET  /api/college/students        ← List college students
POST /api/college/add             ← Add new student
POST /api/college/update          ← Update student record
POST /api/college/delete          ← Delete student
POST /api/college/approve         ← Approve installment
GET  /api/college/download        ← Export as CSV

GET  /api/university/students     ← List university students
GET  /api/university/fee-records  ← Filtered fee records
POST /api/university/add          ← Add new student
POST /api/university/update       ← Update student
POST /api/university/delete       ← Delete student
POST /api/university/approve      ← Approve installment
GET  /api/university/download     ← Export as CSV

GET  /api/stats                   ← Dashboard statistics
```

---

## ⚙️ Configuration (`config.py`)

```python
# University: 8 semesters, 2 installments each
MAX_SEMESTERS    = 8
UNI_INSTALLMENTS = 2

# College: 4 installments per academic year
COLLEGE_INSTALLMENTS = 4

# Fee status values
STATUS_PENDING  = "Pending"
STATUS_APPROVED = "Approved"
```

All department lists, program names, default fees, and Excel sheet names are centralized in `config.py` for easy customization.

---

## 📦 Dependencies

```txt
flask>=3.0.0          # Web framework & REST API
pandas>=2.1.0         # Data manipulation & filtering
openpyxl>=3.1.0       # Excel read/write with styling
agno>=1.0.0           # AI Agent framework
groq>=0.9.0           # Groq API client (LLaMA 3.3)
google-generativeai>=0.7.0  # Gemini API client
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:7B2C2C,50:375623,100:1F4E79&height=120&section=footer&animation=fadeIn" width="100%"/>

**Built with ❤️ for educational institutions**

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Powered by Agno](https://img.shields.io/badge/Powered%20by-Agno%20AI-6C63FF?style=flat-square)](https://github.com/agno-agi/agno)
[![AI Models](https://img.shields.io/badge/AI-Groq%20%7C%20Gemini-F55036?style=flat-square)](https://groq.com)

</div>