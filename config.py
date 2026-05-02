# config.py - System Configuration

EXCEL_FILE = "fees_system.xlsx"

# ── University Departments ──────────────────────────────────────────────────
DEPARTMENTS = [
    "English",
    "Biochemistry",
    "Computer Science",
    "Mathematics",
    "Physics",
    "Chemistry",
    "Business Administration",
    "Psychology",
    "Urdu",
    "Islamiat",
    "Education",
    "Botany",
    "Zoology",
    "Economics",
    "History",
]

# ── College Programs (FA, ICS, ICOM, FSC Medical, FSC Engineering, IT) ─────
COLLEGE_CLASSES = [
    "FA",
    "ICS",
    "ICOM",
    "FSC Medical",
    "FSC Engineering",
    "IT",
]

COLLEGE_SECTIONS = ["A", "B", "C", "D", "E"]

# ── Default Annual Fee per College Program (Rs.) ────────────────────────────
DEFAULT_COLLEGE_FEES = {
    "FA":              15_000,
    "ICS":             18_000,
    "ICOM":            16_000,
    "FSC Medical":     25_000,
    "FSC Engineering": 25_000,
    "IT":              20_000,
}

# ── Default Per-Semester Fee per University Department (Rs.) ─────────────────
DEFAULT_UNI_FEES = {
    "English":                 8_000,
    "Biochemistry":           16_000,
    "Computer Science":       18_000,
    "Mathematics":            10_000,
    "Physics":                13_000,
    "Chemistry":              13_000,
    "Business Administration":14_000,
    "Psychology":             11_000,
    "Urdu":                    8_000,
    "Islamiat":                8_000,
    "Education":               9_500,
    "Botany":                 11_000,
    "Zoology":                11_000,
    "Economics":              10_000,
    "History":                 9_000,
}

# ── Fee Status ──────────────────────────────────────────────────────────────
STATUS_PENDING  = "Pending"
STATUS_APPROVED = "Approved"
ALL_STATUSES    = [STATUS_PENDING, STATUS_APPROVED]

# ── University Settings ─────────────────────────────────────────────────────
MAX_SEMESTERS        = 8
UNI_INSTALLMENTS     = 2        # installments per semester
COLLEGE_INSTALLMENTS = 4        # installments per year

# ── Excel Sheet Names ───────────────────────────────────────────────────────
SHEET_COLLEGE  = "College_Students"
SHEET_UNI      = "University_Students"
SHEET_UNI_FEE  = "University_Fee_Records"

# ── Excel Styling ───────────────────────────────────────────────────────────
COLOR_HEADER_COLLEGE = "1F4E79"   # dark blue
COLOR_HEADER_UNI     = "375623"   # dark green
COLOR_HEADER_FEE     = "7B2C2C"   # dark red
COLOR_APPROVED       = "C6EFCE"   # light green
COLOR_PENDING        = "FFEB9C"   # light yellow
COLOR_COMPLETE       = "BDD7EE"   # light blue
COLOR_ROW_ALT        = "F2F2F2"   # light grey