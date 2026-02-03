"""
Assignment 10 - Question 2

Program: Calculate Sum of First N Numbers
Description:
    This program defines a function to calculate the sum of first N numbers.

Author: Balraj Jagtap
Date: 19/01/2026
"""

"""Function to calculate sum of first N numbers"""
def Sum(No):
    Sum = 0
    for i in range(1, No + 1):
        Sum = Sum + i

    return Sum

"""Main function to get user input and call the sum calculation function"""
def main():
    print("Enter the number :")
    No = int(input())

    Ans = Sum(No)
    print("Sum of First ",No,"Numbers is : ",Ans)
   
""" Special variable __name__ check """
if __name__ == "__main__":
    main()
