# 25. Create a dictionary containing student names and marks. Develop a program to:
# • Add a student 
# • Update marks 
# • Delete a student 
# • Search for a student 
# • Display all students 
# • Find the highest marks 
# • Calculate the average

students = {
    "Harsh": 95,
    "Yash": 88,
    "Prithvi": 92
}

while True:
    print("\n--- Student Management System ---")
    print("1. Add a student")
    print("2. Update marks")
    print("3. Delete a student")
    print("4. Search for a student")
    print("5. Display all students")
    print("6. Find the highest marks")
    print("7. Calculate the average")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = float(input("Enter marks: "))
        students[name] = marks
        print("Student added successfully.")

    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in students:
            marks = float(input("Enter new marks: "))
            students[name] = marks
            print("Marks updated successfully.")
        else:
            print("Student not found.")

    elif choice == "3":
        name = input("Enter student name to delete: ")
        if name in students:
            del students[name]
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    elif choice == "4":
        name = input("Enter student name to search: ")
        if name in students:
            print(f"Student: {name}, Marks: {students[name]}")
        else:
            print("Student not found.")

    elif choice == "5":
        print("\nAll Students:")
        for name, marks in students.items():
            print(f"{name} : {marks}")

    elif choice == "6":
        if students:
            top_student = max(students, key=students.get)
            print(f"Highest Scorer: {top_student} with {students[top_student]} marks")
        else:
            print("No students available.")

    elif choice == "7":
        if students:
            avg = sum(students.values()) / len(students)
            print(f"Average Marks: {avg:.2f}")
        else:
            print("No students available.")

    elif choice == "8":
        print("Exiting program.")
        break
    else:
        print("Invalid choice, try again.")
