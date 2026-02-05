"""
Assignment 12 - Question 4

Program: Print Numbers from 1 to N
Description:
    This program defines a function to print numbers from 1 to N.

Author: Balraj Jagtap
Date: 27/01/2026
"""


"""Function to print numbers from 1 to N"""
def Print_Numbers(Value):
    for i in range(1, Value + 1):
        print(i, end=" ")


"""Main function to get user input and call the print function"""
def main():
    No = int(input("Enter the Number : "))

    Print_Numbers(No)


if __name__ == "__main__":
    main()