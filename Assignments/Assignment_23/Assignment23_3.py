"""
Assignment 23 - Question 3

Program: Numbers Class Operations
Description:
    This program defines a class 'Numbers' with instance variables
    and methods to check:
    - Prime number
    - Perfect number
    - Factors of a number
    - Sum of factors

Author: Balraj Jagtap
Date: 27/01/2026
"""


class Numbers:
    """Class to perform operations on a number"""

    def __init__(self):
        """Constructor to accept number from user"""
        self.value = int(input("Enter number: "))

    def chk_prime(self):
        """Check whether the number is prime or not"""
        if self.value <= 1:
            return False
        for i in range(2, self.value):
            if self.value % i == 0:
                return False
        return True

    def chk_perfect(self):
        """Check whether the number is perfect or not"""
        total = 0
        for i in range(1, self.value):
            if self.value % i == 0:
                total += i
        return total == self.value

    def factors(self):
        """Return list of all factors of the number"""
        return [i for i in range(1, self.value + 1) if self.value % i == 0]

    def sum_factors(self):
        """Return sum of all factors except the number itself"""
        return sum(i for i in range(1, self.value) if self.value % i == 0)


def main():
    obj = Numbers()

    if obj.chk_prime():
        print(f"{obj.value} is a Prime Number")
    else:
        print(f"{obj.value} is Not a Prime Number")

    if obj.chk_perfect():
        print(f"{obj.value} is a Perfect Number")
    else:
        print(f"{obj.value} is Not a Perfect Number")

    print(f"Factors of {obj.value} are: {obj.factors()}")
    print(f"Sum of factors of {obj.value} is: {obj.sum_factors()}")


if __name__ == "__main__":
    main()
