#4. Bank Account System (Class, Object, Constructor)
#A bank wants to manage customer accounts. Create a BankAccount class with a
#constructor to initialize account number and balance. Implement methods to deposit,
#withdraw, and display balance.

# Create BankAccount class
class BankAccount:

    # Constructor
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    # Deposit money
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    # Withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    # Display balance
    def display(self):
        print("Account Number:", self.account_no)
        print("Available Balance:", self.balance)


# Create object
b1 = BankAccount(6304460933, 5000)

# Perform operations
b1.deposit(2000)
b1.withdraw(1000)
b1.display()