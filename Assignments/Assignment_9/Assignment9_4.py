"""
Assignment 9 - Question 4

Program: Calculate Cube of Number
Description:
    This program defines a function to calculate and return the cube of a number.

Author: Balraj Jagtap
Date: 19/01/2026
"""

"""Function to calculate cube of a number"""
def Cube(No):
    Ret = 0
    Ret = No * No * No
    return Ret

"""Main function to get user input and call the cube function"""
def main():
    print("Enter the Number : ")
    No = int(input())

    Ans = Cube(No)
    print("Cube of",No,"is:",Ans)

""" Special variable __name__ check """
if __name__ == "__main__":
    main()    