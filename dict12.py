# 12. Create a dictionary containing student names and marks. Find the student with the lowest marks.

marks = {
    "Harsh": 95,
    "Yash": 88,
    "Prithvi": 92,
    "Shiva": 98,
    "Atharv": 85
}

print("Student Marks:", marks)

lowest_student = min(marks, key=marks.get)
print(f"Lowest Scorer: {lowest_student} with {marks[lowest_student]} marks")
