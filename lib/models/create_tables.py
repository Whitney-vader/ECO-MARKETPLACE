import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('''CREATE TABLE Users
             (user_id INTEGER PRIMARY KEY, username TEXT, email TEXT, password TEXT)''')

c.execute('''CREATE TABLE Products
             (product_id INTEGER PRIMARY KEY, name TEXT, description TEXT, price REAL)''')

c.execute('''CREATE TABLE Cart
             (cart_id INTEGER PRIMARY KEY, user_id INTEGER, product_id INTEGER, quantity INTEGER)''')

c.execute('''CREATE TABLE Ratings
             (rating_id INTEGER PRIMARY KEY, user_id INTEGER, product_id INTEGER, rating REAL)''')

conn.commit()
conn.close()