import hashlib
import sqlite3

def register_user(username, email, password):
    conn = sqlite3.connect('ecomm.db')
    c = conn.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
              (username, email, hashed_password))
    conn.commit()
    conn.close()

def login_user(username, password):
    conn = sqlite3.connect('ecomm.db')
    c = conn.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    c.execute("SELECT * FROM users WHERE username=? AND password=?",
              (username, hashed_password))
    user = c.fetchone()
    conn.close()
    return user

def get_all_products():
    conn = sqlite3.connect('ecomm.db')
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    conn.close()
    return products

def search_product(name):
    conn = sqlite3.connect('ecomm.db')
    c = conn.cursor()
    c.execute("SELECT * FROM products WHERE name LIKE ?", ('%' + name + '%',))
    products = c.fetchall()
    conn.close()
    return products

def add_to_cart(user_id, product_id, quantity):
    conn = sqlite3.connect('ecomm.db')
    c = conn.cursor()
    c.execute("INSERT INTO cart (user_id, product_id, quantity) VALUES (?, ?, ?)",
              (user_id, product_id, quantity))
    conn.commit()
    conn.close()

def get_cart_items(user_id):
    conn = sqlite3.connect('ecomm.db')
    c = conn.cursor()
    c.execute("SELECT * FROM cart WHERE user_id=?", (user_id,))
    cart_items = c.fetchall()
    conn.close()
    return cart_items

def rate_product(user_id, product_id, rating):
    conn = sqlite3.connect('ecomm.db')
    c = conn.cursor()
    c.execute("INSERT INTO ratings (user_id, product_id, rating) VALUES (?, ?, ?)",
              (user_id, product_id, rating))
    conn.commit()
    conn.close()