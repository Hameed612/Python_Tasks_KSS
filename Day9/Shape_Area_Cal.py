# 6. Shape Area Calculator (Polymorphism)
# A graphics application needs to calculate the area of different shapes. Create classes
# Circle, Rectangle, and Triangle, each having an area() method. Demonstrate
# polymorphism by calling the same method for different objects.

# Circle class
class Circle:

    def area(self):
        r = 5
        print("Circle Area:", 3.14 * r * r)


# Rectangle class
class Rectangle:

    def area(self):
        l = 10
        w = 5
        print("Rectangle Area:", l * w)


# Triangle class
class Triangle:

    def area(self):
        b = 10
        h = 5
        print("Triangle Area:", 0.5 * b * h)


# Create objects
c = Circle()
r = Rectangle()
t = Triangle()

# Call the same method
c.area()
r.area()
t.area()