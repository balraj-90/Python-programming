"""
Assignment 12 - Question 3

Program: Basic Arithmetic Operations
Description:
    This program defines functions to perform addition, subtraction, multiplication, and division of two numbers.

Author: Balraj Jagtap
Date: 27/01/2026
"""


"""Function to perform addition, subtraction, multiplication, and division"""
def Addition(No1, No2):
    Ans  = 0
    Ans = No1 + No2
    print("Addition is : ",Ans)

def Subtraction(No1, No2):
    Ans  = 0
    Ans = No1 - No2
    print("Subtraction is : ",Ans)

def Multiplication(No1, No2):
    Ans = 0
    Ans = No1 * No2
    print("Multiplication is : ",Ans)

def Division(No1, No2):
    Ans = 0
    if No2 == 0:
        print("Division by zero is not defined.")
    else:
        Ans = No1 / No2
        print("Division is : ",Ans)


"""Main function to get user input and call the arithmetic functions"""
def main():
    No1 = int(input("Enter the First Number : "))
    No2 = int(input("Enter the Second Number : "))

    Addition(No1, No2)
    Subtraction(No1, No2)   
    Multiplication(No1, No2)
    Division(No1, No2)


if __name__ == "__main__":          # Special variable __name__ check 
    main()