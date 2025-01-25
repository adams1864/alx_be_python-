
class Book:
    def __init__(self, title, author, year):
        """Constructor method to initialize the Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor method that prints a message when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation method that returns a user-friendly string."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation method that returns a string that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"