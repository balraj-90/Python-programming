"""
Assignment 11 - Question 2

Program: Count Digits
Description:
    This program defines a function to count the digits in a number.

Author: Balraj Jagtap
Date: 20/01/2026
"""

"""Function to count the digits in a number"""
def CountDigits(No):
    Count = 0
    
    if No == 0:
        Count = 1
    else:
        while No != 0:
            No = No // 10
            Count += 1
        return Count

"""Main function to get user input and call the digit count function"""
def main():
    print("Enter Number : ")
    No = int(input())

    Ret = CountDigits(No)
    print("Count of Digits is : ", Ret)


""" Special variable __name__ check """
if __name__ == "__main__":
    main()