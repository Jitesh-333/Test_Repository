class Bank:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    # Getter method for name
    def get_name(self):
        return self.__name

    # Setter method for name
    def set_name(self, name):
        self.__name = name

    # Getter method for balance
    def get_balance(self):
        return self.__balance

    # Private method to check if withdrawal is possible
    def __can_withdraw(self, amount):
        return self.__balance >= amount

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    # Method to withdraw money
    def withdraw(self, amount):
        if self.__can_withdraw(amount):
            self.__balance -= amount
            return True
        return False

    # Method to display account details
    def display_account(self):
        return f"Account Name: {self.__name}, Balance: {self.__balance}"

# Creating an object of Bank class
account = Bank("Alice", 1000)

# Accessing account details using public method
print(account.display_account())

# Depositing money
account.deposit(500)
print(account.display_account())

# Withdrawing money
if account.withdraw(300):
    print("Withdrawal successful.")
else:
    print("Insufficient balance.")

print(account.display_account())

# Trying to access private attributes (will raise AttributeError)
try:
    print(account.__balance)
except AttributeError as e:
    print(e)
