"""
Assignment 9 - Question 2

Program: Check Greater Number
Description:
    This program defines a function to check and display the greater number between two inputs.

Author: Balraj Jagtap
Date: 19/01/2026
"""

"""Function to check and display the greater number"""
def ChkGreater(No1, No2):
    if No1 > No2:
        print(No1,"is Greater Number")

    elif No2 > No1:
        print(No2,"is Greater Number")

"""Main function to get user input and call the check function"""
def main():
    print("Enter Two Numbers : ")
    No1 = int(input())
    No2 = int(input())

    ChkGreater(No1, No2)

""" Special variable __name__ check """
if __name__ == "__main__":
    main()    