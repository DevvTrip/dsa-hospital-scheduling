# AI-Based Hospital Appointment Scheduling System

DSA-II Individual Assignment (BCSE0401), NIET, B.Tech AI, Semester 3.

Student: Devvrat Tripathi | Roll No: 250133150078 | Faculty: Mr Vikas Tripathi

## Files

| File | Purpose |
|---|---|
| `hospital_system.c` | Main deliverable: complete C program (about 360 lines), terminal only, no GUI |
| `hospital_system_code.pdf` | Code listing as a PDF (5 pages, line numbers, comment highlighting) for submission |
| `report_final.docx` | Filled PBL report template, ready to convert to PDF and submit |
| `report_final.md` | Same report as plain text, easy to edit if needed |
| `make_report.py` | Script that generated the docx and md; run again after edits |
| `make_code_pdf.py` | Script that rebuilds the code PDF from hospital_system.c |
| `src/` | Old Python drafts of the same algorithms (optional, not part of submission) |

## Compile and run the C program

With gcc (MinGW, Dev C++, CodeBlocks, or Linux):

```
gcc hospital_system.c -o hospital_system
./hospital_system          (Windows: hospital_system.exe)
```

No compiler installed? Paste the code into Online GDB (onlinegdb.com, choose C)
or open it in Dev C++ and press Compile and Run.

## Menu options

1. Show all patients (BST inorder)
2. Search patient by ID
3. Add new patient
4. Show appointment queue (heap)
5. Heap sort patients by severity
6. Shortest path between departments (Dijkstra)
7. OT slot allocation (0/1 knapsack DP)
8. Pack free slot exactly (sum of subsets)
9. Exit

Unit mapping: options 1-5 = Unit 1, option 6 = Unit 2, option 7 = Unit 3,
option 8 = Unit 4. Unit 5 (B+ tree) is analyzed in the report, Module 11.

## About the report

- Built directly from your college template file (Report template.docx), so the
  front page table, declaration, heading style and section order match it exactly.
- Each module has a short theory part (BST property, heap property, Dijkstra
  relaxation, DP subproblems, backtracking pruning, B+ tree leaves), plus the
  work done, output and findings, in simple English.
- Word counts stay inside the IA limits: body total is about 1290 of 1500 words,
  and every section is within its own limit.
- Times New Roman 12 pt, 1.15 line spacing, 1 inch margins.
- The Appendix contains the full source code at 8 pt font, which takes more than
  the 3-page IA appendix limit. If your faculty checks page counts strictly,
  submit hospital_system_code.pdf as the separate code file instead of the
  printed appendix, or keep only the main functions in the appendix.
- Converting to PDF: open report_final.docx in Word, File, Save As, PDF.
  If the PDF is over 500 KB, compress it (smallpdf.com or Word's
  "Minimum size" PDF option), because the total upload limit is 500 KB.
- Plagiarism limit is 20%. The report was written fresh for this topic, but
  before submitting, read it once and rewrite two or three sentences in each
  section in your own words. This also helps during the viva, and it keeps the
  AI-detection risk low. An AI tool usage declaration may be required by your
  faculty, so ask before submitting.

## Submission checklist

- [ ] Topic Approval Form (already filled, get faculty sign)
- [ ] report_final.docx converted to PDF (under 500 KB)
- [ ] hospital_system.c (attached as source code)
- [ ] AI tool usage declaration if faculty asks for one
