# Format: (employee_name, start_hour_24h, end_hour_24h)
shifts = [
    ("Rohan", 9, 13),
    ("Rohan", 12, 16),   # Overlaps 12..13 with first shift
    ("Meera", 8, 12),
    ("Meera", 13, 17),   # Back-to-back (12..13 free) -> no overlap
    ("Meera", 11, 14),   # Overlaps 13..14 with 13..17
    ("Zoya", 10, 18),
]

unique_employees = []
for emp_name, _, _ in shifts:
    if emp_name not in unique_employees:
        unique_employees.append(emp_name)

conflicted_employees = []

for emp in unique_employees:
    emp_intervals = []
    for emp_name, start_h, end_h in shifts:
        if emp_name == emp and start_h < end_h:
            emp_intervals.append((start_h, end_h))

    has_conflict = False
    for i in range(len(emp_intervals)):
        s1, e1 = emp_intervals[i]
        for j in range(i + 1, len(emp_intervals)):
            s2, e2 = emp_intervals[j]
            if s1 < e2 and s2 < e1:
                has_conflict = True
                print(f"Conflict for {emp}: shift {s1}:00-{e1}:00 overlaps with {s2}:00-{e2}:00")

    if has_conflict and emp not in conflicted_employees:
        conflicted_employees.append(emp)

print("\nEmployees with Shift Conflicts:", conflicted_employees)
