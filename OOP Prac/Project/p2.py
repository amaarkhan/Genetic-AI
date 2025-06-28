'''
Project 2: Simple E-commerce System Till 11 pm today
Objective: Create an OOP system to simulate a basic online store, allowing customers to browse products, add them to a shopping cart, and place orders. 

Concepts to Apply: 

Classes & Objects: Product, Customer, ShoppingCart, Order. 

Attributes & Methods: 
Product: Name, price, stock quantity. Methods to check availability, reduce stock. 

Customer: Name, customer ID, contact info. 

ShoppingCart: Stores Product objects and quantities. Methods to add/remove items, calculate total. 

Order: Stores ordered items, total amount, customer info, order status. 


Encapsulation: Make product_id, customer_id, stock_quantity, and order_id private/protected, with public getters/setters or methods for interaction. 

Inheritance (Optional but Recommended): 
Product base class, with subclasses ElectronicProduct (might have warranty info) and ClothingProduct (might have size/color). 

Polymorphism (Optional): If different Product types, a display_details() method could show different info based on the product type. 

Core Features: 
Product Catalog: Add products to the store's catalog. 

Shopping Cart: Customers can add products to their cart, update quantities, remove items. 

Checkout Process: Calculate total cost, simulate placing an order. 

Order Tracking: Basic order status (e.g., "Pending", "Shipped"). 

User Interface: Simple text-based menu for customers to interact. 
'''
# ---------- Product Classes ----------
class Product:
    def __init__(self, product_id, name, price, stock_quantity):
        self._product_id = product_id
        self.name = name
        self.price = price
        self.__stock_quantity = stock_quantity

    def is_available(self, quantity):
        return self.__stock_quantity >= quantity

    def reduce_stock(self, quantity):
        if self.is_available(quantity):
            self.__stock_quantity -= quantity
            return True
        return False

    def get_stock(self):
        return self.__stock_quantity

    def get_product_id(self):
        return self._product_id

    def display_details(self):
        return f"{self.name} - ${self.price} - Stock: {self.__stock_quantity}"


# Optional Inheritance & Polymorphism
class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, stock_quantity, warranty):
        super().__init__(product_id, name, price, stock_quantity)
        self.warranty = warranty

    def display_details(self):
        return f"{self.name} - ${self.price} - Warranty: {self.warranty} years - Stock: {self.get_stock()}"


class ClothingProduct(Product):
    def __init__(self, product_id, name, price, stock_quantity, size, color):
        super().__init__(product_id, name, price, stock_quantity)
        self.size = size
        self.color = color

    def display_details(self):
        return f"{self.name} - ${self.price} - Size: {self.size}, Color: {self.color} - Stock: {self.get_stock()}"


# ---------- Customer ----------
class Customer:
    def __init__(self, customer_id, name, contact_info):
        self._customer_id = customer_id
        self.name = name
        self.contact_info = contact_info

    def get_customer_id(self):
        return self._customer_id


# ---------- ShoppingCart ----------
class ShoppingCart:
    def __init__(self):
        self.items = {}  # key: Product, value: quantity

    def add_item(self, product, quantity):
        if product.is_available(quantity):
            if product in self.items:
                self.items[product] += quantity
            else:
                self.items[product] = quantity
            print(f"Added {quantity} x {product.name} to cart.")
        else:
            print(f"Only {product.get_stock()} units available for {product.name}.")

    def remove_item(self, product):
        if product in self.items:
            del self.items[product]
            print(f"Removed {product.name} from cart.")
        else:
            print("Item not in cart.")

    def calculate_total(self):
        return sum(product.price * quantity for product, quantity in self.items.items())

    def view_cart(self):
        if not self.items:
            print("Cart is empty.")
            return
        for product, quantity in self.items.items():
            print(f"{product.name} - ${product.price} x {quantity}")
        print(f"Total: ${self.calculate_total()}")


# ---------- Order ----------
class Order:
    order_counter = 1

    def __init__(self, customer, cart):
        self.__order_id = Order.order_counter
        Order.order_counter += 1
        self.customer = customer
        self.items = cart.items.copy()
        self.total_amount = cart.calculate_total()
        self.status = "Pending"

        # Reduce stock
        for product, quantity in self.items.items():
            product.reduce_stock(quantity)

    def get_order_id(self):
        return self.__order_id

    def get_status(self):
        return self.status

    def update_status(self, new_status):
        self.status = new_status

    def display_order(self):
        print(f"\nOrder ID: {self.__order_id}")
        print(f"Customer: {self.customer.name}")
        print("Items:")
        for product, quantity in self.items.items():
            print(f"- {product.name} x {quantity}")
        print(f"Total: ${self.total_amount}")
        print(f"Status: {self.status}")


# ---------- Text-Based Interface ----------
def ecommerce_menu():
    catalog = []
    orders = []
    cart = ShoppingCart()
    customer = Customer("C001", "Daddy Buyer", "daddy@hotmail.com")

    # Sample Products
    catalog.append(ElectronicProduct("P001", "Laptop", 999.99, 5, 2))
    catalog.append(ClothingProduct("P002", "T-Shirt", 19.99, 10, "M", "Black"))
    catalog.append(Product("P003", "Book", 12.49, 15))

    while True:
        print("\n--- E-Commerce Menu ---")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. View Orders")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nProduct Catalog:")
            for idx, product in enumerate(catalog, 1):
                print(f"{idx}. {product.display_details()}")

        elif choice == '2':
            print("\nSelect product number to add:")
            for idx, product in enumerate(catalog, 1):
                print(f"{idx}. {product.display_details()}")
            try:
                prod_index = int(input("Enter number: ")) - 1
                quantity = int(input("Quantity: "))
                if 0 <= prod_index < len(catalog):
                    cart.add_item(catalog[prod_index], quantity)
                else:
                    print("Invalid product number.")
            except ValueError:
                print("Invalid input.")

        elif choice == '3':
            print("\nSelect product number to remove:")
            for idx, product in enumerate(cart.items.keys(), 1):
                print(f"{idx}. {product.name}")
            try:
                remove_index = int(input("Enter number: ")) - 1
                product_list = list(cart.items.keys())
                if 0 <= remove_index < len(product_list):
                    cart.remove_item(product_list[remove_index])
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Invalid input.")

        elif choice == '4':
            cart.view_cart()

        elif choice == '5':
            if not cart.items:
                print("Your cart is empty.")
                continue
            order = Order(customer, cart)
            orders.append(order)
            print("Order placed successfully!")
            order.display_order()
            cart = ShoppingCart()  # Reset cart

        elif choice == '6':
            if not orders:
                print("No orders yet.")
            for order in orders:
                order.display_order()

        elif choice == '7':
            print("Thanks for shopping, Daddy 😏")
            break

        else:
            print("Invalid choice. Try again.")


ecommerce_menu()
