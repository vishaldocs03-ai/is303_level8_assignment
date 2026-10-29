import random


class BankAccount:
    """Represents a simple bank account for one customer."""

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.account_number = random.randint(10000, 99999)
        self.balance = 0.00

    def deposit(self, amount):
        """Add money to the account. Returns True if the deposit succeeded."""
        if amount <= 0:
            print("Deposit amount must be greater than $0.00.")
            return False

        self.balance += amount
        print(f"Deposited ${amount:,.2f}. New balance: ${self.balance:,.2f}")
        return True

    def withdraw(self, amount):
        """Remove money from the account. Returns True if the withdrawal succeeded."""
        if amount <= 0:
            print("Withdrawal amount must be greater than $0.00.")
            return False

        if amount > self.balance:
            print(f"Insufficient funds. Your current balance is ${self.balance:,.2f}.")
            return False

        self.balance -= amount
        print(f"Withdrew ${amount:,.2f}. New balance: ${self.balance:,.2f}")
        return True

    def display_account_info(self):
        """Print the customer's name, account number, and current balance."""
        print(f"Name: {self.customer_name}")
        print(f"Account #: {self.account_number}")
        print(f"Balance: ${self.balance:,.2f}")
