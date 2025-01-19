class Book:
    """Class representing a book in the library."""
    
    def __init__(self, title, author):
        """Initialize a book with title, author, and set the book as available."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Initially, the book is available
    
    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Return the book and mark it as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out

    def __str__(self):
        """Return a string representation of the book."""
        status = "Available" if self.is_available() else "Checked Out"
        return f"{self.title} by {self.author} ({status})"


class Library:
    """Class representing the library that manages a collection of books."""
    
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Add a book to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title, if it's available."""
        for book in self._books:
            if book.title == title and book.check_out():
                return f"'{title}' has been checked out."
        return f"'{title}' is unavailable or doesn't exist."

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title and book.return_book():
                return f"'{title}' has been returned."
        return f"'{title}' was not checked out or doesn't exist."

    def list_available_books(self):
        """List all books that are available."""
        available_books = [str(book) for book in self._books if book.is_available()]
        if not available_books:
            print("No books available.")
        else:
            print("\n".join(available_books))


# Example usage (provided in the prompt)
if __name__ == "__main__":
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    print("\nChecking out '1984':")
    print(library.check_out_book("1984"))
    print("Available books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    print("\nReturning '1984':")
    print(library.return_book("1984"))
    print("Available books after returning '1984':")
    library.list_available_books()
