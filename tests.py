from library import LibraryManagementSystem, Book, User

# Створення бібліотеки та книг
library = LibraryManagementSystem()

# Додавання книг
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("Mr. Mercedes", "Stephen King", 2014)
library.add_book(book1)
library.add_book(book2)

# Реєстрація користувачів
user1 = User("Alice", "123 Main St", "alice@example.com")
library.register_user(user1)

# Позика книг
library.borrow_book(user1, book1)

# Спроба взяти ту ж книгу повторно
library.borrow_book(user1, book1)

# Пошук книг за автором
print("\nКниги George Orwell:")
library.search_books(lambda book: book.get_author() == "George Orwell")

# Повернення книг
library.return_book(user1, book1)

# Спроба повернути книгу, якої немає у користувача
library.return_book(user1, book2)