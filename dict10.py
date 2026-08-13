# 10. Accept five student names and their marks from the user and store them in a dictionary.

student_marks = {}

for i in range(1, 6):
    name = input(f"Enter name of student {i}: ")
    marks = float(input(f"Enter marks of {name}: "))
    student_marks[name] = marks

print("\nStudent Marks Dictionary:")
print(student_marks)
