# 11. Create a dictionary containing student names and marks. Find the student who has scored the highest marks.

marks = {
    "Harsh": 95,
    "Yash": 88,
    "Prithvi": 92,
    "Shiva": 98,
    "Atharv": 85
}

print("Student Marks:", marks)

highest_student = max(marks, key=marks.get)
print(f"Highest Scorer: {highest_student} with {marks[highest_student]} marks")
