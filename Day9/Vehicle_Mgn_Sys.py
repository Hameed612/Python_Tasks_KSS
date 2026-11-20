# Parent class
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