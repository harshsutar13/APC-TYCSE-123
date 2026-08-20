#23. Create a set containing available books and another set containing requested books. Determine which requested books are available.

available_books = {"Python Programming", "Data Structures", "Web Development", "Operating Systems"}
requested_books = {"Data Structures", "Machine Learning", "Python Programming", "Networking"}

available_requested = requested_books.intersection(available_books)
print("Requested books that are available:", available_requested)
