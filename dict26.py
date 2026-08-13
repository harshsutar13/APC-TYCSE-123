# 26. Create a dictionary containing employee names and salaries. Find:
# • Highest salary 
# • Lowest salary 
# • Average salary 
# • Employees earning more than ₹50,000

employees = {
    "Harsh": 75000,
    "Yash": 45000,
    "Prithvi": 60000,
    "Shiva": 90000,
    "Atharv": 40000
}

print("Employee Salaries:", employees)

# Highest salary
top_emp = max(employees, key=employees.get)
print(f"\nHighest Salary: {top_emp} with ₹{employees[top_emp]}")

# Lowest salary
low_emp = min(employees, key=employees.get)
print(f"Lowest Salary: {low_emp} with ₹{employees[low_emp]}")

# Average salary
avg_salary = sum(employees.values()) / len(employees)
print(f"Average Salary: ₹{avg_salary:.2f}")

# Employees earning more than ₹50,000
high_earners = {name: sal for name, sal in employees.items() if sal > 50000}
print("\nEmployees earning more than ₹50,000:")
for name, sal in high_earners.items():
    print(f"{name} : ₹{sal}")
