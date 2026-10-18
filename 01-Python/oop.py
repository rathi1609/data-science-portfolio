# Python Object-Oriented Programming (OOP)

class Student:
    def __init__(self, name, course, skills):
        self.name = name
        self.course = course
        self.skills = skills

    def introduce(self):
        print(f"Hi, I am {self.name}.")
        print(f"I am learning {self.course}.")
        print("My skills:", ", ".join(self.skills))

    def add_skill(self, skill):
        self.skills.append(skill)


# Create a student object
student1 = Student(
    "Kirti",
    "Data Science",
    ["Python", "SQL"]
)

student1.introduce()

student1.add_skill("Machine Learning")

print("\nAfter learning a new skill:")
student1.introduce()
