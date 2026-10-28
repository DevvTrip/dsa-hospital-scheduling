"""Builds hospital_system_code.pdf: the C source listing as a clean PDF."""

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

BASE = r"C:/Users/devis/Documents/Qoder/2026-10-28/a8ac5a0d/dsa-hospital-scheduling"
SRC = BASE + r"/hospital_system.c"
OUT = BASE + r"/hospital_system_code.pdf"

with open(SRC, encoding="utf-8") as f:
    code_lines = f.read().rstrip("\n").split("\n")
code_lines = [l.encode("ascii", "replace").decode() for l in code_lines]

W, H = A4
LEFT = 36
RIGHT = 30
TOP = 50
BOTTOM = 42
FONT = "Courier"
SIZE = 7.4
LEADING = 9.6
CODE_X = 64
NUM_X = 54
MAX_CHARS = int((W - RIGHT - CODE_X) / (0.6 * SIZE))

c = canvas.Canvas(OUT, pagesize=A4)
c.setTitle("AI-Based Hospital Appointment Scheduling System - Source Code")
c.setAuthor("Devvrat Tripathi")

page = [0]

def page_header(first=False):
    c.setFont("Helvetica", 7.5)
    c.setFillGray(0.45)
    c.drawString(LEFT, H - 26, "AI-Based Hospital Appointment Scheduling System - Source Code (hospital_system.c)")
    c.drawRightString(W - RIGHT, H - 26, f"Page {page[0]}")
    c.setFillGray(0)
    return H - TOP

def page_footer():
    c.setFont("Helvetica", 7.5)
    c.setFillGray(0.45)
    c.drawCentredString(W / 2, 24, "Devvrat Tripathi | Roll 250133150078 | DSA-II (BCSE0401) | Individual Assignment")
    c.setFillGray(0)

def is_comment(line):
    s = line.strip()
    return s.startswith("/*") or s.startswith("*/") or s.startswith("*")

y = None

# title block on page 1
page[0] = 1
y = page_header()
c.setFont("Helvetica-Bold", 15)
c.drawString(LEFT, y - 26, "AI-Based Hospital Appointment Scheduling System")
c.setFont("Helvetica", 10.5)
c.drawString(LEFT, y - 44, "Source Code Listing (hospital_system.c), terminal application in C, no GUI")
c.setFont("Helvetica", 8.5)
c.setFillGray(0.3)
c.drawString(LEFT, y - 60, "Devvrat Tripathi   |   Roll No. 250133150078   |   B.Tech AI, Semester 3, Section B")
c.drawString(LEFT, y - 73, "Course: Data Structures and Algorithms - II (BCSE0401)   |   Faculty: Mr Vikas Tripathi")
c.setFillGray(0)
y -= 96
c.setStrokeGray(0.6)
c.line(LEFT, y, W - RIGHT, y)
y -= 16
c.setFont(FONT, SIZE)

wrapped = []  # (line number or None, text)
for idx, line in enumerate(code_lines, 1):
    if len(line) > MAX_CHARS:
        wrapped.append((idx, line[:MAX_CHARS]))
        rest = line[MAX_CHARS:]
        while rest:
            wrapped.append((None, "        " + rest[:MAX_CHARS - 8]))
            rest = rest[MAX_CHARS - 8:]
    else:
        wrapped.append((idx, line))

for num, line in wrapped:
    if y < BOTTOM:
        page_footer()
        c.showPage()
        page[0] += 1
        y = page_header()
        c.setFont(FONT, SIZE)
    if num is not None:
        c.setFont("Helvetica", 6.5)
        c.setFillGray(0.5)
        c.drawRightString(NUM_X, y, str(num))
    if is_comment(line):
        c.setFillColorRGB(0.10, 0.28, 0.45)
    else:
        c.setFillGray(0)
    c.setFont(FONT, SIZE)
    c.drawString(CODE_X, y, line)
    c.setFillGray(0)
    y -= LEADING

y -= 8
if y < BOTTOM + 20:
    page_footer()
    c.showPage()
    page[0] += 1
    y = page_header()
c.setFont("Helvetica-Oblique", 8)
c.setFillGray(0.4)
c.drawString(LEFT, y, f"End of source code ({len(code_lines)} lines). Compile with: gcc hospital_system.c -o hospital_system")
c.setFillGray(0)
page_footer()
c.save()
print("Created:", OUT, "| pages:", page[0], "| max chars per line:", MAX_CHARS)
