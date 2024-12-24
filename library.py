class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"


class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book}.")
        else:
            print(f"Sorry, {book} is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book}.")
        else:
            print(f"{self.name} does not have {book}.")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book} to the library.")

    def list_books(self):
        print("Books in the library:")
        for book in self.books:
            status = "Available" if book.is_available else "Not Available"
            print(f"- {book} ({status})")
