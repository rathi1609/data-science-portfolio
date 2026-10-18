# Python Lists and Dictionaries

# List of student marks
marks = [85, 90, 78, 92, 88]

print("Student Marks:", marks)
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
print("Average Marks:", sum(marks) / len(marks))

# Student information using a dictionary
student = {
    "name": "Kirti",
    "subject": "Data Science",
    "skills": ["Python", "SQL", "Machine Learning"]
}

print("\nStudent Name:", student["name"])
print("Subject:", student["subject"])
print("Skills:")

for skill in student["skills"]:
    print("-", skill)
