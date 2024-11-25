class Library:
    def __init__(self):
        self.books = []  # List to store book records (each record is a dictionary)

    def add_book(self, title, author, genre):
        """Add a new book to the library."""
        book = {
            "Title": title,
            "Author": author,
            "Genre": genre,
            "Status": "Available"
        }
        self.books.append(book)
        print(f"Book '{title}' by {author} has been added successfully!")

    def view_books(self):
        """Display all books in the library."""
        print("\n====== Library Books ======")
        if not self.books:
            print("No books available in the library.")
        else:
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. Title: {book['Title']}, Author: {book['Author']}, Genre: {book['Genre']}, Status: {book['Status']}")
        print("================================")

    def search_book(self, title):
        """Search for a book by title."""
        for book in self.books:
            if book["Title"].lower() == title.lower():
                print(f"Book Found: Title: {book['Title']}, Author: {book['Author']}, Genre: {book['Genre']}, Status: {book['Status']}")
                return book
        print(f"Book '{title}' not found in the library.")
        return None

    def borrow_book(self, title):
        """Borrow a book by title."""
        book = self.search_book(title)
        if book:
            if book["Status"] == "Available":
                book["Status"] = "Borrowed"
                print(f"You have successfully borrowed the book '{title}'.")
            else:
                print(f"Sorry, the book '{title}' is already borrowed.")

    def return_book(self, title):
        """Return a borrowed book by title."""
        book = self.search_book(title)
        if book:
            if book["Status"] == "Borrowed":
                book["Status"] = "Available"
                print(f"You have successfully returned the book '{title}'.")
            else:
                print(f"The book '{title}' is not currently borrowed.")

def main():
    library = Library()
    while True:
        print("\n====== Library Management System ======")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book by Title")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")
        print("=======================================")

        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.")
            continue

        if choice == 1:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            genre = input("Enter book genre: ")
            library.add_book(title, author, genre)

        elif choice == 2:
            library.view_books()

        elif choice == 3:
            title = input("Enter the title of the book to search: ")
            library.search_book(title)

        elif choice == 4:
            title = input("Enter the title of the book to borrow: ")
            library.borrow_book(title)

        elif choice == 5:
            title = input("Enter the title of the book to return: ")
            library.return_book(title)

        elif choice == 6:
            print("Exiting the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()

