# Case Study 48: Tuple-Based Employee Shift Conflict Detection

## Problem Statement

Represent employee shifts as tuples, detect overlapping shift intervals for each employee, and list employees with scheduling conflicts.

## Objectives

* Store shift records using tuples and unpack start/end times cleanly.

* Compare all pairs of shifts per employee to catch overlaps.

## Assumptions

* Each shift is `(employee_name, start_hour, end_hour)` using 24-hour integers (`0` to `24`), where `start_hour < end_hour`.

* Two intervals $[s_1, e_1)$ and $[s_2, e_2)$ overlap if $s_1 < e_2$ and $s_2 < e_1$.

## Algorithm

1. Store shifts in a list of tuples.

2. Extract unique employee names into a list.

3. For each employee, gather their shifts `(start, end)` and check every pair `(i, j)` with `j > i` for overlap.

4. Report conflicting employees and their overlapping shifts.

## Flowchart

```
[Start] --> [Load Shift Tuples] --> [For Each Employee]
  --> [Collect Shift Pairs] --> [Compare Pairs (s1 < e2 and s2 < e1)]
  --> [Overlap Found? (Yes -> Flag Conflict)] --> [Print Report] --> [End]

```

## Pseudocode

```
BEGIN
    shifts = [("Rohan", 9, 13), ("Rohan", 12, 16), ("Meera", 8, 12), ("Meera", 13, 17)]
    employees = []
    FOR name, s, e IN shifts DO
        IF name NOT IN employees THEN APPEND name TO employees END IF
    END FOR
    FOR emp IN employees DO
        emp_shifts = []
        FOR name, s, e IN shifts DO
            IF name == emp THEN APPEND (s, e) TO emp_shifts END IF
        END FOR
        # Check pairs for overlap
    END FOR
END

```

## Test Cases & Expected Output

* **Test Case 1 (Mixed schedules):** Rohan and Meera have overlapping intervals; Zoya has a single shift and no conflicts.

```
Conflict for Rohan: shift 9:00-13:00 overlaps with 12:00-16:00
Conflict for Meera: shift 13:00-17:00 overlaps with 11:00-14:00

Employees with Shift Conflicts: ['Rohan', 'Meera']

```

## Conclusion

Immutable tuples with tuple unpacking keep schedule records structured while simple interval comparison catches overlaps reliably.
