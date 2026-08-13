# 13. Create a dictionary containing student names and marks. Calculate the average marks of all students.

marks = {
    "Harsh": 95,
    "Yash": 88,
    "Prithvi": 92,
    "Shiva": 98,
    "Atharv": 85
}

print("Student Marks:", marks)

total_marks = sum(marks.values())
average_marks = total_marks / len(marks)

print("Average Marks:", average_marks)
