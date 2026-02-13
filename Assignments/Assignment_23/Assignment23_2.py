"""
Assignment 23 - Question 2

Program: Bank Account Management System
Description:
    This program defines a class 'BankAccount' which performs
    basic banking operations such as:
    - Display account details
    - Deposit money
    - Withdraw money
    - Calculate interest

Author: Balraj Jagtap
Date: 27/01/2026
"""


class BankAccount:
    """Class representing a bank account"""

    rate_of_interest = 10.5     # Class variable

    def __init__(self, name, amount):
        """Constructor to initialize account details"""
        self.name = name
        self.amount = amount

    def display(self):
        """Display account holder details"""
        print("Account Holder Name :", self.name)
        print("Account Balance     :", self.amount)

    def deposit(self):
        """Deposit amount into account"""
        amt = int(input("Enter amount to deposit: "))
        self.amount += amt
        print(f"Amount {amt} deposited successfully.")
        print(f"Updated Balance: {self.amount}")

    def withdraw(self):
        """Withdraw amount from account"""
        amt = int(input("Enter amount to withdraw: "))
        if amt > self.amount:
            print("Insufficient Balance")
        else:
            self.amount -= amt
            print(f"Amount {amt} withdrawn successfully.")
            print(f"Updated Balance: {self.amount}")

    def calculate_interest(self):
        """Calculate interest on current balance"""
        interest = (self.amount * BankAccount.rate_of_interest) / 100
        print(
            f"Interest at {BankAccount.rate_of_interest}% is: {interest}"
        )


def main():
    obj = BankAccount("Marvellous", 1000)

    obj.display()
    obj.deposit()
    obj.withdraw()
    obj.calculate_interest()


if __name__ == "__main__":
    main()
