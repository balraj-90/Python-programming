"""
Assignment 9 - Question 5

Program: Check Divisibility
Description:
    This program defines a function to check divisibility.

Author: Balraj Jagtap
Date: 19/01/2026
"""

"""Function to check divisibility of a number by 3 and 5"""
def CheckDivisibility(No):
    if(No % 5 == 0) and (No % 3 == 0):
        print("The Number is Divisible by 3 and 5")
    elif(No % 3 == 0):
        print("The Number is Divisible by 3")
    elif(No % 5 == 0):
        print("The Number is Divisible by 5")

"""Main function to get user input and call the divisibility check function"""
def main():
    print("Enter the Number : ")
    No = int(input())

    CheckDivisibility(No)

""" Special variable __name__ check """
if __name__ == "__main__":
    main()    