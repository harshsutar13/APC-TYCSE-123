# 29. Create a dictionary containing book IDs and book names.
# Implement:
# • Add a book 
# • Search a book 
# • Remove a book 
# • Display all books 
# • Count total books

books = {
    "B101": "Python Programming",
    "B102": "Data Structures",
    "B103": "Operating Systems"
}

while True:
    print("\n--- Book Management System ---")
    print("1. Add a book")
    print("2. Search a book")
    print("3. Remove a book")
    print("4. Display all books")
    print("5. Count total books")
    print("6. Exit")

    choice = input("Enter choice (1-6): ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        books[book_id] = title
        print("Book added.")

    elif choice == "2":
        book_id = input("Enter Book ID to search: ")
        if book_id in books:
            print(f"Book ID: {book_id}, Title: {books[book_id]}")
        else:
            print("Book not found.")

    elif choice == "3":
        book_id = input("Enter Book ID to remove: ")
        if book_id in books:
            del books[book_id]
            print("Book removed.")
        else:
            print("Book not found.")

    elif choice == "4":
        print("\nAll Books:")
        for book_id, title in books.items():
            print(f"{book_id} : {title}")

    elif choice == "5":
        print(f"Total Books: {len(books)}")

    elif choice == "6":
        print("Exiting.")
        break
    else:
        print("Invalid choice!")
