import controllers

def main():
    while True:
        print("Eco-Marketplace CLI")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            username = input("Enter username: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            controllers.register_user(username, email, password)
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = controllers.login_user(username, password)
            if user:
                while True:
                    print("1. View products")
                    print("2. Search for a product")
                    print("3. Add to cart")
                    print("4. View cart")
                    print("5. Rate a product")
                    print("6. Logout")
                    choice = input("Enter your choice: ")
                    
                    if choice == "1":
                        products = controllers.get_all_products()
                        for product in products:
                            print(product)
                            print(product)
                            print(product)
                    elif choice == "2":
                        name = input("Enter product name to search: ")
                        products = controllers.search_product(name)
                        if products:
                            for product in products:
                                print(product)
                        else:
                            print("No products found with that name.")
                    elif choice == "3":
                        product_id = input("Enter product ID to add to cart: ")
                        quantity = input("Enter quantity: ")
                        controllers.add_to_cart(user[0], product_id, quantity)
                    elif choice == "4":
                        cart_items = controllers.get_cart_items(user[0])
                        for item in cart_items:
                            print(item)
                    elif choice == "5":
                        product_id = input("Enter product ID to rate: ")
                        rating = input("Enter rating: ")
                        controllers.rate_product(user[0], product_id, rating)
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