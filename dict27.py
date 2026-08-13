# 27. Create a dictionary containing product names and quantities.
# Perform:
# • Add a product 
# • Update quantity 
# • Delete a product 
# • Search for a product 
# • Display products with quantity below 10

products = {
    "Laptop": 15,
    "Mouse": 5,
    "Keyboard": 8,
    "Monitor": 12,
    "USB Cable": 3
}

while True:
    print("\n--- Product Quantity Management ---")
    print("1. Add a product")
    print("2. Update quantity")
    print("3. Delete a product")
    print("4. Search for a product")
    print("5. Display products with quantity below 10")
    print("6. Exit")

    choice = input("Enter choice (1-6): ")

    if choice == "1":
        name = input("Enter product name: ")
        qty = int(input("Enter quantity: "))
        products[name] = qty
        print("Product added.")

    elif choice == "2":
        name = input("Enter product name to update: ")
        if name in products:
            qty = int(input("Enter new quantity: "))
            products[name] = qty
            print("Quantity updated.")
        else:
            print("Product not found.")

    elif choice == "3":
        name = input("Enter product name to delete: ")
        if name in products:
            del products[name]
            print("Product deleted.")
        else:
            print("Product not found.")

    elif choice == "4":
        name = input("Enter product name to search: ")
        if name in products:
            print(f"Product: {name}, Quantity: {products[name]}")
        else:
            print("Product not found.")

    elif choice == "5":
        print("\nProducts with quantity below 10:")
        low_stock = False
        for name, qty in products.items():
            if qty < 10:
                print(f"{name} : {qty}")
                low_stock = True
        if not low_stock:
            print("No products with quantity below 10.")

    elif choice == "6":
        print("Exiting program.")
        break
    else:
        print("Invalid choice!")
