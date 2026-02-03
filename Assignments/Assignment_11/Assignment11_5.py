"""
Assignment 11 - Question 5

Program: Check Palindrome Number
Description:
    This program defines a function to check if a number is palindrome.

Author: Balraj Jagtap
Date: 20/01/2026
"""

"""Function to check if a number is palindrome"""
def Palindrome(No):
    if No < 0 :
        return False
    Original = No
    Rev = 0 
    while No != 0:
        Digit = No % 10
        Rev = Rev * 10 + Digit
        No = No // 10

    if Original == Rev:
        return True
    else:
        return False

"""Main function to get user input and call the palindrome check function"""
def main():
    print("Enter Number : ")
    No = int(input())

    Ret = Palindrome(No)
    if Ret:
        print("It is a Palindrome Number")
    else:
        print("It is not a Palindrome Number")


""" Special variable __name__ check """
if __name__ == "__main__":
    main()