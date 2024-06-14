import sqlite3
from models import User

def create_tables():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Users
                  (user_id INTEGER PRIMARY KEY, username TEXT NOT NULL, email TEXT NOT NULL, password TEXT NOT NULL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS Products
                  (product_id INTEGER PRIMARY KEY, name TEXT NOT NULL, description TEXT, price REAL NOT NULL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS Cart
                  (cart_id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL, product_id INTEGER NOT NULL, quantity INTEGER NOT NULL DEFAULT 1)''')
    c.execute('''CREATE TABLE IF NOT EXISTS Ratings
                  (rating_id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL, product_id INTEGER NOT NULL, rating INTEGER NOT NULL)''')
    conn.commit()
    conn.close()

def add_products():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    products = [
        ("Product 1", "Description 1", 10.99),
        ("Product 2", "Description 2", 9.99),
        ("Product 3", "Description 3", 12.99),
        ("Product 4", "Description 4", 8.99),
        ("Product 5", "Description 5", 11.99),
        ("Product 6", "Description 6", 13.99),
        ("Product 7", "Description 7", 10.99),
        ("Product 8", "Description 8", 9.99),
        ("Product 9", "Description 9", 12.99),
        ("Product 10", "Description 10", 8.99)
    ]
    c.executemany("INSERT INTO Products (name, description, price) VALUES (?,?,?)", products)
    conn.commit()
    conn.close()

def register_user(username, email, password):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO Users (username, email, password) VALUES (?,?,?)", (username, email, password))
    conn.commit()
    conn.close()
    print("User registered successfully!")

def login_user(username, password):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Users WHERE username=? AND password=?", (username, password))
    user_data = c.fetchone()
    conn.close()
    if user_data:
        return User(*user_data)  # Create a new User object with the data
    else:
        return None
    
def view_products():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Products")
    products = c.fetchall()
    if products:
        print("Available Products:")
        for product in products:
            print(f"Product ID: {product[0]}, Name: {product[1]}, Price: {product[2]}")
    else:
        print("No products available")
    conn.close()
    input("Press Enter to continue...")

def search_product(product_name):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Products WHERE name LIKE?", ('%' + product_name.lower() + '%',))
    products = c.fetchall()
    if products:
        for product in products:
            print(f"Product ID: {product[0]}, Name: {product[1]}, Description: {product[2]}, Price: {product[3]}")
    else:
        print("Product not found")
    conn.close()
    input("Press Enter to continue...")
    
def add_to_cart(user_id):
    product_id = input("Enter product ID to add to cart: ")
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Products WHERE product_id=?", (product_id,))
    product = c.fetchone()
    if product:
        c.execute("SELECT * FROM Cart WHERE user_id=? AND product_id=?", (user_id, product_id))
        cart_item = c.fetchone()
        if cart_item:
            c.execute("UPDATE Cart SET quantity=quantity+1 WHERE user_id=? AND product_id=?", (user_id, product_id))
        else:
            c.execute("INSERT INTO Cart (user_id, product_id, quantity) VALUES (?,?,1)", (user_id, product_id))
        conn.commit()
        print("Product added to cart successfully")
    else:
        print("Product not found")
    conn.close()
    input("Press Enter to continue...")
    
def view_cart(user_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Cart WHERE user_id=?", (user_id,))
    cart_data = c.fetchall()
    conn.close()
    if cart_data:
        print("Your cart:")
        for item in cart_data:
            print(f"Product ID: {item[1]}, Name: {item[2]}, Price: {item[3]}")
    else:
        print("Your cart is empty.")

def rate_product(user_id, product_id, rating):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO Ratings (user_id, product_id, rating) VALUES (?,?,?)", (user_id, product_id, rating))
    conn.commit()
    conn.close()