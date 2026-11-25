
student_name = "Ananya Rao"
subjects = ["Math", "Physics", "Chemistry", "English", "CS"]
raw_marks = [32, 78, 33, 84, 68]
max_marks = 100
pass_mark = 35
grace_available = 10
max_grace_per_subject = 5

final_marks = []
grace_used_total = 0

for mark in raw_marks:
    updated = mark
    if mark < pass_mark and grace_available > 0:
        deficit = pass_mark - mark
        allowable = grace_available
        if allowable > max_grace_per_subject:
            allowable = max_grace_per_subject
        add_grace = deficit if deficit < allowable else allowable

        if updated + add_grace <= max_marks:
            updated = updated + add_grace
            grace_available = grace_available - add_grace
            grace_used_total = grace_used_total + add_grace
    final_marks.append(updated)

all_passed = True
for m in final_marks:
    if m < pass_mark:
        all_passed = False

percentage = (sum(final_marks) / (len(subjects) * max_marks)) * 100

if not all_passed:
    classification = "Fail"
elif percentage >= 75:
    classification = "Distinction"
elif percentage >= 60:
    classification = "First Class"
else:
    classification = "Pass"

print(f"Student: {student_name}")
for i in range(len(subjects)):
    print(f"  {subjects[i]}: {raw_marks[i]} -> {final_marks[i]}")
print(f"Grace Used: {grace_used_total} | Percentage: {percentage:.2f}% | Result: {classification}")
