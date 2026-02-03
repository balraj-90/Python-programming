"""
Assignment 10 - Question 4

Program: Display Table of Even Numbers till N
Description:
    This program defines a function to display even numbers till N.

Author: Balraj Jagtap
Date: 20/01/2026
"""

"""Function to display multiplication table of a number"""
def EvenNumbers(No):
    for i in range (1, No + 1):
        if (i % 2 == 0):
            print(i)

"""Main function to get user input and call the table display function"""
def main():
    print("Enter the number till which Even Nos are to be printed :")
    No = int(input())

    EvenNumbers(No)
    
""" Special variable __name__ check """
if __name__ == "__main__":
    main()
