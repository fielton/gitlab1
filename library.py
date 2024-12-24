from abc import ABC, abstractmethod

# Інтерфейс "Книга"
class IBook(ABC):
    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def get_author(self):
        pass

    @abstractmethod
    def get_year(self):
        pass

    @abstractmethod
    def is_available(self):
        pass

# Інтерфейс "Читач"
class IUser(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_address(self):
        pass

    @abstractmethod
    def get_contact_info(self):
        pass

    @abstractmethod
    def get_borrowed_books(self):
        pass

# Інтерфейс "Система управління бібліотекою"
class ILibraryManagementSystem(ABC):
    @abstractmethod
    def add_book(self, book):
        pass

    @abstractmethod
    def register_user(self, user):
        pass

    @abstractmethod
    def borrow_book(self, user, book):
        pass

    @abstractmethod
    def return_book(self, user, book):
        pass

    @abstractmethod
    def search_books(self, criterion):
        pass

# Реалізація інтерфейсу "Книга"
class Book(IBook):
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_year(self):
        return self.year

    def is_available(self):
        return self.available

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"

# Реалізація інтерфейсу "Читач"
class User(IUser):
    def __init__(self, name, address, contact_info):
        self.name = name
        self.address = address
        self.contact_info = contact_info
        self.borrowed_books = []

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_contact_info(self):
        return self.contact_info

    def get_borrowed_books(self):
        return self.borrowed_books

# Реалізація інтерфейсу "Система управління бібліотекою"
class LibraryManagementSystem(ILibraryManagementSystem):
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
            print(f"Книга {book} додана до бібліотеки.")
        else:
            print(f"Книга {book} вже існує в бібліотеці.")

    def register_user(self, user):
        if user not in self.users:
            self.users.append(user)
            print(f"Користувач {user.get_name()} зареєстрований.")
        else:
            print(f"Користувач {user.get_name()} вже зареєстрований.")

    def borrow_book(self, user, book):
        if book in self.books and book.is_available():
            book.available = False
            user.get_borrowed_books().append(book)
            print(f"Книга {book} видана користувачу {user.get_name()}.")
        else:
            print(f"Книга {book} недоступна або не знайдена.")

    def return_book(self, user, book):
        if book in user.get_borrowed_books():
            book.available = True
            user.get_borrowed_books().remove(book)
            print(f"Книга {book} повернута до бібліотеки користувачем {user.get_name()}.")
        else:
            print(f"Користувач {user.get_name()} не позичав книгу {book}.")

    def search_books(self, criterion):
        found_books = [book for book in self.books if criterion(book)]
        for book in found_books:
            status = "Доступна" if book.is_available() else "Недоступна"
            print(f"- {book} ({status})")


