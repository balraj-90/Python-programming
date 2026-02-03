"""
Assignment 10 - Question 3

Program: Calculate Factorial of a Number
Description:
    This program defines a function to calculate the factorial of a number.

Author: Balraj Jagtap
Date: 20/01/2026
"""

""""Function to calculate factorial of a number"""
def Factorial(No): 
    Fact = 1
    for i in range(1, No + 1):
        Fact = Fact * i 

    return Fact

"""Main function to get user input and call the factorial calculation function"""
def main():
    print("Enter the number :")
    No = int(input())

    Ans = Factorial(No)
    print("Factorial of",No,"is :",Ans)
    
    
""" Special variable __name__ check """
if __name__ == "__main__":
    main()
