# 5. Vehicle Management System (Inheritance)
#A transport company manages different vehicles. Create a base class Vehicle with
#attributes like brand and speed. Create derived classes Car and Bike that inherit from
#Vehicle and display their details.

# Base class
class Vehicle:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed


# Child class Car
class Car(Vehicle):

    def display(self):
        print("Car Brand:", self.brand)
        print("Car Speed:", self.speed)


# Child class Bike
class Bike(Vehicle):

    def display(self):
        print("Bike Brand:", self.brand)
        print("Bike Speed:", self.speed)


# Create objects
c1 = Car("Toyota", 120)
b1 = Bike("Honda", 100)

# Display details
c1.display()
b1.display()