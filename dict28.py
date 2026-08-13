# 28. Create a dictionary containing names and phone numbers.
# Implement:
# • Add contact 
# • Search contact 
# • Update contact 
# • Delete contact 
# • Display all contacts

contacts = {
    "Harsh": "9876543210",
    "Yash": "9123456789"
}

while True:
    print("\n--- Phonebook Management ---")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Display all contacts")
    print("6. Exit")

    choice = input("Enter choice (1-6): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added.")

    elif choice == "2":
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"Name: {name}, Phone: {contacts[name]}")
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter name to update: ")
        if name in contacts:
            phone = input("Enter new phone number: ")
            contacts[name] = phone
            print("Contact updated.")
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("\nAll Contacts:")
        for name, phone in contacts.items():
            print(f"{name} : {phone}")

    elif choice == "6":
        print("Exiting phonebook.")
        break
    else:
        print("Invalid choice!")
