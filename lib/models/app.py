import sqlite3
from faker import Faker
from controllers import register_user, login_user, view_products, search_product, add_to_cart, view_cart, rate_product

def seed_data():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    products = [
        ("Product 1", "Description 1", 10.99),
        ("Product 2", "Description 2", 9.99),
        ("Product 3", "Eco-friendly product 3", 12.99),
        ("Product 4", "Eco-friendly product 4", 8.99),
        ("Product 5", "Eco-friendly product 5", 11.99),
        ("Product 6", "Eco-friendly product 6", 10.99),
        ("Product 7", "Eco-friendly product 7", 9.99),
        ("Product 8", "Eco-friendly product 8", 12.99),
        ("Product 9", "Eco-friendly product 9", 8.99),
        ("Product 10", "Eco-friendly product 10", 11.99),
    ]
    c.execute("DELETE FROM Products")
    for product in products:
        c.execute("INSERT INTO Products (name, description, price) VALUES (?,?,?)", product)
    conn.commit()
    conn.close()
    print("Database seeded with sample data")

def main():
    while True:
        print("Eco-Marketplace")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            username = input("Enter username: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            register_user(username, email, password)
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = login_user(username, password)
            if user:
                print("Login successful!")
                while True:
                    print("1. View products")
                    print("2. Search for a product")
                    print("3. Add to cart")
                    print("4. View cart")
                    print("5. Rate a product")
                    print("6. Logout")
                    choice = input("Enter your choice: ")
                    if choice == "1":
                        view_products()
                    elif choice == "2":
                        product_name = input("Enter product name to search: ")
                        search_product(product_name)
                    elif choice == "3":
                        add_to_cart(user.id)
                    elif choice == "4":
                        view_cart(user.id)
                    elif choice == "5":
                        product_id = int(input("Enter product ID to rate: "))
                        rating = int(input("Enter your rating (1-5): "))
                        rate_product(user.id, product_id, rating)  # Pass the user_id, product_id, and rating arguments
                    elif choice == "6":
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Invalid username or password. Please try again.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()