# 16. Library Management System (Constructor & Inheritance)
# A library stores information about books and digital books. Create a base class Book
# with a constructor to initialize book details. Create a derived class EBook that adds file
# size information.

# Explanation:
# - Book is the parent class.
# - EBook is the child class.
# - super() calls the parent constructor.
# - EBook adds its own file_size attribute.

# Parent class
class Book:

    # Constructor
    def __init__(self, title, author):
        self.title = title
        self.author = author


# Child class
class EBook(Book):

    # Constructor
    def __init__(self, title, author, file_size):

        # Call parent constructor
        super().__init__(title, author)

        self.file_size = file_size

    # Display book details
    def display(self):
        print("Book Title:", self.title)
        print("Author:", self.author)
        print("File Size:", self.file_size, "MB")


# Create object
b1 = EBook("Python Programming", "John", 5)

# Display details
b1.display()