"""
Assignment 11 - Question 1

Program: Check Prime Number
Description:
    This program defines a function to check if a number is prime.

Author: Balraj Jagtap
Date: 20/01/2026
"""

"""Function to check if a number is prime"""
def Check_Prime(No):
    if No <= 1:
        return False
    for i in range(2, int(No ** 0.5) + 1):
        if No % i == 0:
            return False
    return True

"""Main function to get user input and call the prime check function"""
def main():
    print("Enter Number : ")
    No = int(input())

    Ret = Check_Prime(No)
    if Ret:
        print("It is a Prime Number")
    else:
        print("It is not a Prime Number")


""" Special variable __name__ check """
if __name__ == "__main__":
    main()