import library_func

def main():
    """
    Главная функция, выводящая меню и подсказки для взаимодействия пользователя с функционалом приложения.
    """
    library = library_func.Library()

    while True:
        print("\n----------Меню----------")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выход")
        print("-------------------------")

        choice = input("Выберите действие (цифра): ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            try:
                year = int(input("Введите год издания книги (число): "))
                library.add_book(title, author, year)
            except ValueError:
                print("Ошибка: неверный формат года")

        elif choice == '2':
            try:
                book_id = int(input("Введите id книги для удаления: "))
                library.delete_book(book_id)
            except ValueError:
                print("Ошибка: неверный формат id")

        elif choice == '3':
            search = input("Введите название, автора или год для поиска: ")
            found_book = library.find_book(search)
            if found_book:
                for book in found_book:
                    print(book)
            else:
                print("Книга не найдена")

        elif choice == '4':
            library.show_books()

        elif choice == '5':
            try:
                book_id = int(input("Введите id книги: "))
                new_status = input("Введите новый статус (в наличии или выдана): ")
                library.change_status(book_id, new_status)
            except ValueError:
                print("Ошибка: неверный формат id")
            
        elif choice == '6':
            break
        else:
            print("Пожалуйста, выберите действие из меню")

if __name__ == "__main__":
    main()