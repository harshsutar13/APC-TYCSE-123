#6. Create a dictionary of employee IDs and names. Ask the user for an employee ID and check whether it exists. 

emp = {
    "101":"harsh",
    "102":"yash",
    "103":"prithvi",
    "104":"shiva",
    "105":"atharv"
}

print(emp)
key = input("Enter emp id to delete :")

if key in emp:
    print("Employee found")
    print(key, emp[key])

else:
    print("employee not found")

