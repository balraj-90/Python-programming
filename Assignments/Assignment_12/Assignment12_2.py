"""
Assignment 12 - Question 2

Program: Factors of a Number
Description:
    This program defines a function to print all factors of a given number.

Author: Balraj Jagtap
Date: 27/01/2026
"""


"""Function to print factors of a number"""
def print_factors(Number):
    print("Factors are : ")
    for i in range(1, Number + 1):
        if Number % i == 0:
            print(i)


"""Main function to get user input and call the check function"""
def main():
    No = int(input("Enter the Number : "))

    print_factors(No)


if __name__ == "__main__":
    main()