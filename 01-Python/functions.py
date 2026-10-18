# Python Functions Practice

def greet(name):
    return f"Hello, {name}! Welcome to Python."

def add_numbers(a, b):
    return a + b

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


print(greet("Kirti"))
print("Sum:", add_numbers(10, 20))

marks = [85, 90, 78, 92, 88]
print("Average marks:", calculate_average(marks))
