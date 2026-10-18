# Python File Handling Practice

# Write data to a file
with open("student.txt", "w", encoding="utf-8") as file:
    file.write("Name: Kirti\n")
    file.write("Field: Data Science\n")
    file.write("Skill: Python\n")

print("Data written successfully!")

# Read data from the file
with open("student.txt", "r", encoding="utf-8") as file:
    content = file.read()

print("\nFile Content:")
print(content)

# Append new information
with open("student.txt", "a", encoding="utf-8") as file:
    file.write("Skill: Machine Learning\n")

print("New information added!")
