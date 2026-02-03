"""
Assignment 10 - Question 5

Program: Display Odd Numbers till N
Description:
    This program defines a function to display odd numbers till N.

Author: Balraj Jagtap
Date: 20/01/2026
"""

"""Function to display multiplication table of a number"""
def OddNumbers(No):
    for i in range(1 , No + 1):
        if(i % 2 != 0 ):
            print(i)

"""Main function to get user input and call the odd numbers display function"""
def main():
    print("Enter the number till which Odd Nos are to be printed :")
    No = int(input())

    OddNumbers(No)
    
""" Special variable __name__ check """
if __name__ == "__main__":
    main()
