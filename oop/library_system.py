class Book:
    def __init__(self, title, author):
        """Constructor method to initialize book attributes."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation of a Book."""
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        """Constructor method for EBook, with an additional file_size attribute."""
        super().__init__(title, author)  # Calling the parent class constructor
        self.file_size = file_size

    def __str__(self):
        """String representation of an EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Constructor method for PrintBook, with an additional page_count attribute."""
        super().__init__(title, author)  # Calling the parent class constructor
        self.page_count = page_count

    def __str__(self):
        """String representation of a PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        """Constructor method for Library that initializes an empty book list."""
        self.books = []

    def add_book(self, book):
        """Adds a book (or derived book) to the library."""
        self.books.append(book)

    def list_books(self):
        """Lists all books in the library, printing their details."""
        for book in self.books:
            print(book)
