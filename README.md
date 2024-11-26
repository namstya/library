# Консольное приложение для управления библиотекой

## Описание
Консольное приложение для управления библиотекой книг.  
Приложение позволяет добавлять, удалять, искать и отображать книги.  
Каждая книга содержит следующие поля:  
 * id (уникальный идентификатор, генерируется автоматически)
 * title (название книги)
 * author (автор книги)
 * year (год издания)
 * status (статус книги: “в наличии”, “выдана”

---
## Функционал
1. Добавление книги: Пользователь вводит title, author и year, после чего
 книга добавляется в библиотеку с уникальным id истатусом “в наличии”.
2. Удаление книги: Пользователь вводит idкниги, которую нужно удалить.
3. Поиск книги: Пользователь может искать книги по title, author или year.
4. Отображение всех книг: Приложениевыводитсписоквсехкнигсихid, title, author, year и status.
5. Изменение статуса книги: Пользователь вводит id книги и новый статус (“в наличии” или“выдана”).
Данные хранятся в json файле. Есть обработка ошибок.

---
## Инструкция по использованию
### Запуск приложения
1. Скачайте и установите Python.
2. Скачайте репозиторий.
3. Запустите приложение в консоли с помощью команды `python main.py`

### Использование приложения
При запуске приложения отобразится меню.  
```
----------Меню----------
1. Добавить книгу
2. Удалить книгу
3. Поиск книги
4. Отобразить все книги
5. Изменить статус книги
6. Выход
-------------------------
Выберите действие (цифра):
```
#### Добавление книги в библиотеку
1. Введите цифру 1.
2. Введите название книги.  
3. Введите автора книги.  
4. Введите год издания книги. Если введен некорректный год, то выведется ошибка.  
5. Если все верно, то в библиотеку добавится книга и на экране будет выведено уведомление об этом.  
   `Книга 'title' добавлена в библиотеку`
   
#### Удаление книги из библиотеки
1. Введите цифру 2.  
2. Введите id книги для удаления. Если книги с таким id нет, то выведется ошибка. Если некорректый id, то выведется ошибка.  
3. Если все верно, то книга удалится из библиотеки и на экране будет выведено уведомление об этом.  
   `Книга 'title' удалена из библиотеки`

#### Поиск книги в библиотеке
1. Введите цифру 3.
2. Введите название, автора или год для поиска книги. Если нет книги с таким значением, то выведется информация о том, что такая книга не найдена.  
3. Если все верно, то в консоль выведутся все книги с подходящим значением.

#### Отобразить все книги
1. Введите цифру 4.  
2. В консоль выведутся все книги со всей информацией о них.

#### Изменить статус книги
1. Выберите цифру 5.  
2. Введите id книги для которой хотите изменить статус. При некорректном id выведется ошибка.  
3. Введите новый статус. Статус может быть только 'в наличии' или 'выдана'. При неккоректном значении выведется ошибка.

#### Выход из программы
1. Введите цифру 6.
2. Произойдет завершение программы.
