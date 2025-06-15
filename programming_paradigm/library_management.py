# library_management.py
class Book:
    """A class of book to represent the title and author of a book"""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """Marks the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False # Was not checked out

    def is_available(self):
        """Returns True if the book is available, False otherwise."""
        return not self._is_checked_out

    def __str__(self):
        """Returns a string representation of the book."""
        return f"{self.title} by {self.author}"
    
class Library:
    def __init__(self):
        self._books = []
    def add_book(self, book):
        """Adds a Book object to the library's collection."""
        if isinstance(book, Book):
            self._books.append(book)
            print(f"Added '{book.title}' to the library.")
        else:
            print("Error: Only Book objects can be added to the library.")

    def check_out_book(self, title):
        """
        Checks out a book by title. Marks it as unavailable.
        Returns True if successful, False otherwise.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Checked out '{title}'.")
                return True
        print(f"'{title}' is not available for checkout or does not exist.")
        return False

    def return_book(self, title):
        """
        Returns a book by title. Marks it as available again.
        Returns True if successful, False otherwise.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Returned '{title}'.")
                return True
        print(f"'{title}' was not checked out or does not exist.")
        return False

    def list_available_books(self):
        """Lists all books currently available in the library."""
        available_found = False
        for book in self._books:
            if book.is_available():
                print(f"   {book}")
                available_found = True
        if not available_found:
            print("   No books are currently available.")
