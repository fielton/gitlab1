from library import Library, Book, User

# Створення бібліотеки та книг
library = Library()
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book3 = Book("Mr. Mercedes", "Stephen King", 2014)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Створення користувача
user = User("Alice")

# Взаємодія користувача з бібліотекою
library.list_books()
user.borrow_book(book1)
user.borrow_book(book2)

library.list_books()
user.return_book(book1)
library.list_books()