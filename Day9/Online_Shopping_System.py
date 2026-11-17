# 9. Online Shopping System (Multilevel Inheritance)
# An e-commerce company organizes products using multiple levels. Create classes
# Product → ElectronicProduct → MobilePhone using multilevel inheritance and
# display product details.

# Explanation:- MobilePhone inherits from ElectronicProduct, which inherits from Product.
# This is multilevel inheritance.

# Parent class
class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


# Child class
class ElectronicProduct(Product):

    def electronic_details(self):
        print("Product Type: Electronic")


# Grandchild class
class MobilePhone(ElectronicProduct):

    def display(self):
        print("Product Name:", self.name)
        print("Price:", self.price)
        self.electronic_details()


# Create object
m1 = MobilePhone("iPhone 18 pro max", 200000)

# Display details
m1.display()
