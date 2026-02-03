"""
Assignment 11 - Question 4

Program: Reverse a Number
Description:
    This program defines a function to reverse a number.

Author: Balraj Jagtap
Date: 20/01/2026
"""

"""Function to reverse a number"""
def ReverseNumber(No):
    Rev = 0

    if No == 0:
        Rev = 0
    else:
        while No != 0:
            Digit = No % 10
            Rev = Rev * 10 + Digit
            No = No // 10

        return Rev

"""Main function to get user input and call the reverse number function"""
def main():
    print("Enter Number : ")
    No = int(input())

    Ret = ReverseNumber(No)
    print("Reverse of Number is : ", Ret)


""" Special variable __name__ check """
if __name__ == "__main__":
    main()