#2. Rectangle Area Calculator (Constructor) A geometry application needs to calculate the area of rectangles.
# Create a Rectangle
#class that uses a constructor to initialize length and width. Add a method to calculate
#and display the area.

# Create Rectangle class
class Rectangle:

    # Constructor
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to calculate area
    def area(self):
        result = self.length * self.width
        print("Area of Rectangle:", result)


# Create object
r1 = Rectangle(10, 5)

# Call area method
r1.area()