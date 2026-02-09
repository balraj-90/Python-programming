"""
Assignment 13 - Question 4

Program: Print Binary Number
Description:
    This program defines a function to print the binary representation of a number.

Author: Balraj Jagtap
Date: 28/01/2026
"""


"""Function to print binary representation of a number"""
def Print_Binary(Value):
    if Value > 1:
        Print_Binary(Value // 2)
    print(Value % 2, end="")


"""Main function to get user input and call the print function"""
def main():
    Number = int(input("Enter the Number : "))
    Print_Binary(Number)


""" Special variable __name__ check """
if __name__ == "__main__":
    main()