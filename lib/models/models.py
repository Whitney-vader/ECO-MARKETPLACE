class User:
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

class CartItem:
    def __init__(self, user_id, product_id, quantity):
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity

class Rating:
    def __init__(self, user_id, product_id, rating):
        self.user_id = user_id
        self.product_id = product_id
        self.rating = rating
