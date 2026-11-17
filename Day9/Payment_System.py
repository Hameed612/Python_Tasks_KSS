# 11. Payment System (Runtime Polymorphism)
# An online store supports multiple payment methods: CreditCard, UPI, and
# NetBanking. Create a base class Payment with a method process_payment() and
# override it in each payment type.

# Explanation: Each child class overrides the parent class method.
# The method that runs depends on the object.

# Parent class
class Payment:

    def process_payment(self):
        print("Processing Payment")


# Child class 1
class CreditCard(Payment):

    def process_payment(self):
        print("Payment through Credit Card")


# Child class 2
class UPI(Payment):

    def process_payment(self):
        print("Payment through UPI")


# Child class 3
class NetBanking(Payment):

    def process_payment(self):
        print("Payment through Net Banking")


# Create objects
p1 = CreditCard()
p2 = UPI()
p3 = NetBanking()

# Call methods
p1.process_payment()
p2.process_payment()
p3.process_payment()