patients = (
    (101, "Rahul", 25, "A+"),
    (102, "Amit", 30, "B+"),
    (103, "Sneha", 22, "O+"),
    (104, "Priya", 28, "A+")
)


print("Patient Records:")

for patient in patients:
    print(patient)


patient_id = int(input("\nEnter Patient ID to search: "))

found = False

for patient in patients:
    if patient[0] == patient_id:
        print("Patient Found:")
        print("ID:", patient[0])
        print("Name:", patient[1])
        print("Age:", patient[2])
        print("Blood Group:", patient[3])
        found = True

if found == False:
    print("Patient not found")


print("\nTotal Number of Patients =", len(patients))


blood_group = input("\nEnter Blood Group: ")

print("Patients with Blood Group", blood_group)

for patient in patients:
    if patient[3] == blood_group:
        print(patient)
