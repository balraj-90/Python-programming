"""
Assignment 10 - Question 1

Program: Display Table of a Number
Description:
    This program defines a function to display a multiplication table.

Author: Balraj Jagtap
Date: 19/01/2026
"""

"""Function to display multiplication table of a number"""
def Table(No):
    for i in range (1, 11):
        Ans = No * i
        print(No," * ",i," = ",Ans)

"""Main function to get user input and call the table display function"""
def main():
    print("Enter the number of which the table has to displayed :")
    No = int(input())

    Table(No)

""" Special variable __name__ check """
if __name__ == "__main__":
    main()
