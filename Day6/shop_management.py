# Small Shop Customer Purchase Management System

# Dictionary: Store product names and prices
products = {
    "Pen": 10,
    "Notebook": 50,
    "Pencil": 5,
    "Eraser": 5
}

# List: Store cart items
cart = []

# Set: Store product categories
categories = {"Stationery", "Writing", "Books"}

# Tuple: Store product details
product_details = (
    ("Pen", 10, "Writing"),
    ("Notebook", 50, "Books"),
    ("Pencil", 5, "Writing"),
    ("Eraser", 5, "Stationery")
)


# Function 1: Display available products
def display_products():

    print("\nAvailable Products:")

    for name, price in products.items():
        print(name, ":", price)


# Function 2: Add items to cart
def add_to_cart():

    try:
        name = input("Enter product name: ")

        # Check product availability
        if name not in products:
            raise NameError

        # Get quantity from user
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        # Store product name, price and quantity
        item = (name, products[name], quantity)

        cart.append(item)

        print("Item added to cart successfully.")

    except ValueError:
        print("Invalid quantity! Please enter a number.")

    except NameError:
        print("Product not found in store.")


# Function 3: Recursive function to calculate total price
def calculate_total(items):

    # Check cart data type
    if not isinstance(items, list):
        raise TypeError

    # Base condition
    if len(items) == 0:
        return 0

    # Check item data type
    item = items[0]

    if not isinstance(item, tuple) or len(item) != 3:
        raise TypeError

    name, price, quantity = item

    if not isinstance(price, (int, float)):
        raise TypeError

    if not isinstance(quantity, int):
        raise TypeError

    # Calculate current item price
    current_total = price * quantity

    # Recursive calculation
    return current_total + calculate_total(items[1:])


# Function 4: Display cart and total bill
def calculate_bill():

    try:
        if len(cart) == 0:
            print("Your cart is empty.")
            return

        print("\nItems in Cart:")

        # Display all cart items
        for name, price, quantity in cart:
            print(name, "x", quantity)

        # Calculate total using recursion
        total = calculate_total(cart)

        print("Total Bill:", total)

    except TypeError:
        print("Cart data type error.")

    except ZeroDivisionError:
        print("Calculation error: division by zero.")


# Main Menu
while True:

    print("\n1. Display Products")
    print("2. Add Item to Cart")
    print("3. View Total Bill")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            display_products()

        elif choice == 2:
            add_to_cart()

        elif choice == 3:
            calculate_bill()

        elif choice == 4:
            print("Thank you for shopping!")
            break

        else:
            print("Invalid choice! Please select 1 to 4.")

    except ValueError:
        print("Please enter a valid menu number.")
