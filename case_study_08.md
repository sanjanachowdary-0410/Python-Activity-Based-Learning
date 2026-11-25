# Case Study 42: Student Marks Matrix Analysis

## Problem Statement
Analyze a nested list (matrix) of student marks across subjects to compute student averages, identify the top performer, compute subject averages, and flag subjects with low average performance ($< 50$).

## Objectives
* Traverse a 2D list using nested loops.
* Compute row-wise (student) and column-wise (subject) statistics.
* Highlight top student and low-scoring subjects.

## Assumptions
* Rows represent students; columns represent subjects.
* Every row has the same length as `subjects`.

## Algorithm
1. Define `students`, `subjects`, and `marks_matrix` (nested list).
2. Loop over each student row to calculate total and average; track highest average student.
3. Loop over each subject column to calculate subject average; flag averages below `50.0`.
4. Print all results clearly.

## Flowchart
```text
[Start] --> [Load Students, Subjects & Matrix] --> [Row Loop: Student Totals & Topper]
  --> [Col Loop: Subject Averages & Low Flags (<50)] --> [Print Report] --> [End]
```

## Pseudocode
```text
BEGIN
    students = ["Aarav", "Diya", "Kabir", "Meera"]
    subjects = ["Math", "Science", "English", "History"]
    matrix = [[88, 76, 81, 79], [42, 48, 70, 55], [92, 89, 85, 90], [45, 44, 62, 49]]
    # Row averages
    # Column averages
    # Identify top student and subjects with avg < 50
END
```

## Test Cases & Expected Output
* **Test Case 1 ($4$ students $\times$ $4$ subjects):** Kabir leads at `89.00`; subject averages are computed across all four subjects.

```text
--- Student Averages ---
Aarav: Avg = 81.00
Diya: Avg = 53.75
Kabir: Avg = 89.00
Meera: Avg = 50.00

Top Performer: Kabir (89.00)

--- Subject Averages & Weak Subjects (< 50.0) ---
Math: Avg = 66.75
Science: Avg = 64.25
English: Avg = 74.50
History: Avg = 68.25
```

## Conclusion
Row-major and column-major traversal over nested lists makes both individual and subject-wide analytics clean to compute.
