# Student Marks Analyzer

students = {
    "Aarav": [85, 90, 78],
    "Priya": [92, 88, 95],
    "Rahul": [55, 60, 58],
    "Kirti": [95, 91, 98]
}

PASS_MARKS = 40

print("===== STUDENT MARKS ANALYZER =====\n")

averages = {}

for name, marks in students.items():
    average = sum(marks) / len(marks)
    averages[name] = average

    result = "Pass" if all(
        mark >= PASS_MARKS for mark in marks
    ) else "Fail"

    print(f"Student: {name}")
    print(f"Marks: {marks}")
    print(f"Average: {average:.2f}")
    print(f"Result: {result}\n")

top_student = max(averages, key=averages.get)

all_marks = [
    mark
    for marks in students.values()
    for mark in marks
]

print("===== CLASS SUMMARY =====")
print(f"Class Average: {sum(all_marks) / len(all_marks):.2f}")
print(f"Highest Mark: {max(all_marks)}")
print(f"Lowest Mark: {min(all_marks)}")
print(f"Top Student: {top_student}")
