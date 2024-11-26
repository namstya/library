import json

class Book:
    """
    Класс инициализирует книгу с атрибутами: book_id, title, author, year, status.
    """
    def __init__(self, book_id, title, author, year, status="в наличии"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    """
    Метод для вывода строки с информацией о книге.
    """
    def __str__(self):
        return f'{self.book_id}. "{self.title}" {self.author} ({self.year} г.) - {self.status}'

class Library:
    """
    Класс для управления списком книг в библиотеке.
    """
    def __init__(self):
        self.books = []
        self.load_books()

    def load_books(self):
        """
        Функция для загрузки данных из json файла.
        """
        try:
            with open("library.json", "r", encoding="utf-8") as file:
                data = json.load(file)
                self.books = [Book(**book) for book in data]
        except (FileNotFoundError):
            print("Ошибка: не найден файл")
            pass

    def save_books(self):
        """
        Функция для загрузки данных в json файл.
        """
        with open("library.json", "w", encoding="utf-8") as file:
            data = [book.__dict__ for book in self.books]
            json.dump(data, file, indent=4, ensure_ascii=False)

    def add_book(self, title, author, year):
        """
        Функция для добавления книги в библиотеку.

        title: Название книги.
        author: Автор книги.
        year: Год издания книги.
        """
        book_id = max([book.book_id for book in self.books], default=0) + 1
        new_book = Book(book_id, title, author, year)
        self.books.append(new_book)
        self.save_books()
        print(f"Книга '{title}' добавлена в библиотеку")

    def delete_book(self, book_id):
        """
        Функция для удаления книги из библиотеки.

        book_id: уникальный идентификатор книги.
        """
        book_to_remove = next((book for book in self.books if book.book_id == book_id), None)
        if book_to_remove:
            self.books.remove(book_to_remove)
            self.save_books()
            print(f"Книга '{book_to_remove.title}' удалена из библиотеки")
        else:
            print("Ошибка: книга с таким id не найдена")
     
    def find_book(self, search):
        """
        Функция для поиска книги в библиотеке.

        search: аргумент поиска книги по title, author или year.
        """
        found_book = []
        for book in self.books:
            if (search.lower() in book.title.lower() or search.lower() in book.author.lower() or search in str(book.year)):
                found_book.append(book)
        return found_book

    def show_books(self):
        """
        Функция для отображения всех книг в библиотеке.
        """
        if not self.books:
            print("Библиотека пуста")
        else:
            for book in self.books:
                print(book)

    def change_status(self, book_id, new_status):
        """
        Функция для изменения статуса книги в библиотеке.
        """
        book = next((book for book in self.books if book.book_id == book_id), None)
        if book:
            if new_status in ["в наличии", "выдана"]:
                book.status = new_status
                self.save_books()
            else:
                print("Ошибка: статус должен быть 'в наличии' или 'выдана'")
        else:
            print("Ошибка: книга с таким id не найдена")
