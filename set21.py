#21. Find students enrolled in both courses and students enrolled in only one course.

python_students = {"Alice", "Bob", "Charlie", "David"}
java_students = {"Charlie", "David", "Eve", "Frank"}

# Enrolled in both courses
both_courses = python_students.intersection(java_students)
print("Students enrolled in both courses:", both_courses)

# Enrolled in only one course
only_one_course = python_students.symmetric_difference(java_students)
print("Students enrolled in only one course:", only_one_course)
