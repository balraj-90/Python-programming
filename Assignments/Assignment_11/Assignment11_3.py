"""
Assignment 11 - Question 3

Program: Sum of Digits
Description:
    This program defines a function to sum the digits in a number.

Author: Balraj Jagtap
Date: 20/01/2026
"""

"""Function to sum the digits of a number"""
def SumDigits(No):
    Sum = 0

    if No == 0:
        Sum = 0
    else:
        while No != 0:
            Digit = No % 10
            Sum = Sum + Digit
            No = No // 10

        return Sum

"""Main function to get user input and call the sum digits function"""
def main():
    print("Enter Number : ")
    No = int(input())

    Ret = SumDigits(No)
    print("Sum of Digits is : ", Ret)


""" Special variable __name__ check """
if __name__ == "__main__":
    main()