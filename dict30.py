# 30. Take a dictionary containing student names and their departments; create a new dictionary that groups students according to their department.

students = {
    "Harsh": "CSE",
    "Yash": "ECE",
    "Prithvi": "CSE",
    "Shiva": "ME",
    "Atharv": "ECE"
}

print("Original Dictionary (Student -> Dept):", students)

grouped = {}
for name, dept in students.items():
    if dept not in grouped:
        grouped[dept] = []
    grouped[dept].append(name)

print("\nGrouped Dictionary (Dept -> Students):")
print(grouped)
