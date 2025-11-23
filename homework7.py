import sqlite3

# Функция для создания таблицы
def create_table():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    """)

    conn.commit()
    conn.close()


# Функция для вставки данных
def insert_books():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    books = [
        ("Гарри Поттер и философский камень", "Джоан Роулинг", 1997, "Фэнтези", 320, 5),
        ("Властелин колец", "Толкин", 1954, "Фэнтези", 1178, 3),
        ("Преступление и наказание", "Ф. Достоевский", 1866, "Роман", 672, 4),
        ("1984", "Джордж Оруэлл", 1949, "Антиутопия", 328, 6),
        ("Мастер и Маргарита", "Булгаков", 1967, "Роман", 470, 2),
        ("Шерлок Холмс", "Артур Конан Дойл", 1892, "Детектив", 350, 5),
        ("Три мушкетера", "А. Дюма", 1844, "Приключения", 700, 3),
        ("Оно", "Стивен Кинг", 1986, "Ужасы", 1138, 2),
        ("Алхимик", "Пауло Коэльо", 1988, "Философия", 208, 7),
        ("Голодные игры", "Сьюзен Коллинз", 2008, "Фантастика", 384, 5)
    ]

    cursor.executemany("""
        INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
        VALUES (?, ?, ?, ?, ?, ?)
    """, books)

    conn.commit()
    conn.close()


# Запуск функций
if __name__ == "__main__":
    create_table()
    insert_books()
    print("Таблица создана и книги добавлены!")