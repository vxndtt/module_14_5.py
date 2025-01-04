import sqlite3

def initiate_db():
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY, 
            title TEXT NOT NULL,
            description TEXT, 
            price INTEGER NOT NULL
        )
    ''')

    #cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",("Product1", "Описание продукта 1", 100))
    #cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", ("Product2", "Описание продукта 2", 200))
    #cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", ("Product3", "Описание продукта 3", 300))
    #cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",("Product4", "Описание продукта 4", 400))

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users(
                id INTEGER PRIMARY KEY, 
                username TEXT NOT NULL,
                email TEXT NOT NULL, 
                age INTEGER NOT NULL,
                balance INTEGER NOT NULL DEFAULT 1000
            )
        ''')

    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()
    cursor.execute('SELECT id, title, description, price FROM Products')
    products = cursor.fetchall()
    connection.close()
    return products

def add_user(username, email, age):
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, 1000)",
                   (username, email, age))
    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()
    cursor.execute('SELECT COUNT(1) FROM Users WHERE username = ?', (username,))
    user_exists = cursor.fetchone()[0] > 0
    connection.close()

    return user_exists