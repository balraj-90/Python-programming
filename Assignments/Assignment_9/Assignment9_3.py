"""
Assignment 9 - Question 3

Program: Calculate Square of Number
Description:
    This program defines a function to calculate and return the square of a number.

Author: Balraj Jagtap
Date: 19/01/2026
"""

"""Function to calculate square of a number"""
def Square(No):
    Ret = 0
    Ret = No * No
    return Ret

"""Main function to get user input and call the square function"""
def main():
    print("Enter the Number : ")
    No = int(input())

    Ans = Square(No)
    print("Square of",No,"is:",Ans)

""" Special variable __name__ check """
if __name__ == "__main__":
    main()    