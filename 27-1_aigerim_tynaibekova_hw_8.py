import sqlite3

def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)

    return connection


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def insert_product(conn, product):
    try:
        sql = '''INSERT INTO products
        (product_title, price, quantity)
        VALUES (?, ?, ?)
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def add_products(conn):
    products = [('Жидкое мыло с запахом ванили', 75.0, 20),
                ('Мыло детское', 50.0, 30),
                ('Шампунь с экстрактом кедра', 120.0, 10),
                ('Кондиционер для волос', 150.0, 5),
                ('Зубная паста с мятой', 80.0, 50),
                ('Зубная щетка для детей', 50.0, 40),
                ('Детский шампунь 2 в 1', 70.0, 25),
                ('Крем для рук', 90.0, 15),
                ('Дезодорант для женщин', 100.0, 20),
                ('Дезодорант для мужчин', 100.0, 20),
                ('Гель для душа', 110.0, 10),
                ('Лосьон после бритья', 130.0, 5),
                ('Одеколон для женщин', 200.0, 8),
                ('Одеколон для мужчин', 200.0, 8),
                ('Туалетная вода', 300.0, 3)]
    for product in products:
        insert_product(conn, product)
    print('Products added successfully')


def update_quantity(conn, product_id, quantity):
    try:
        sql = '''UPDATE products
        SET quantity = ?
        WHERE id = ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, (quantity, product_id))
        conn.commit()
        print('Quantity updated successfully')
    except sqlite3.Error as e:
        print(e)


def update_price(conn, product_id, price):
    try:
        sql = '''UPDATE products
        SET price = ?
        WHERE id = ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, (price, product_id))
        conn.commit()
        print('Price updated successfully')
    except sqlite3.Error as e:
        print(e)


def delete_product(conn, product_id):
    try:
        sql = '''DELETE FROM products
        WHERE id = ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, (product_id,))
        conn.commit()
        print('Product deleted successfully')
    except sqlite3.Error as e:
        print(e)


def select_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_products_under_100(conn):
    try:
        sql = '''SELECT * FROM products
        WHERE price < 100 AND quantity > 5
        '''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def search_product_by_title(conn, title):
    try:
        sql = '''SELECT * FROM products
        WHERE product_title LIKE ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, ('%'+title+'%',))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


sql_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER NOT NULL DEFAULT 0
)
'''

connection = create_connection('hw.db')
if connection is not None:
    print('Connected successfully')
    # create_table(connection, sql_create_products_table)
    add_products(connection)
    update_quantity(connection, 3, 7)
    update_price(connection, 10, 150)
    delete_product(connection, 1)
    select_all_products(connection)
    search_product_by_title(connection, 'мыло')

    connection.close()