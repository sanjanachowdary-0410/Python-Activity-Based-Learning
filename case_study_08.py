students = ["Aarav", "Diya", "Kabir", "Meera"]
subjects = ["Math", "Science", "English", "History"]

# Rows = students, Columns = subjects
marks_matrix = [
    [88, 76, 81, 79],
    [42, 48, 70, 55],
    [92, 89, 85, 90],
    [45, 44, 62, 49],
]

print("--- Student Averages ---")
top_student = ""
top_avg = -1.0

for r in range(len(marks_matrix)):
    row_sum = 0
    for c in range(len(marks_matrix[r])):
        row_sum += marks_matrix[r][c]
    avg = row_sum / len(marks_matrix[r])
    print(f"{students[r]}: Avg = {avg:.2f}")
    if avg > top_avg:
        top_avg = avg
        top_student = students[r]

print(f"\nTop Performer: {top_student} ({top_avg:.2f})")

print("\n--- Subject Averages & Weak Subjects (< 50.0) ---")
num_students = len(marks_matrix)
for c in range(len(subjects)):
    col_sum = 0
    for r in range(num_students):
        col_sum += marks_matrix[r][c]
    subj_avg = col_sum / num_students
    status = " [LOW AVERAGE]" if subj_avg < 50.0 else ""
    print(f"{subjects[c]}: Avg = {subj_avg:.2f}{status}")
