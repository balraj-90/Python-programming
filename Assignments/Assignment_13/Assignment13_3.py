"""
Assignment 13 - Question 3

Program: Check Perfect Number
Description:
    This program defines a function to check if a number is a perfect number.

Author: Balraj Jagtap
Date: 28/01/2026
"""

"""Function to check if a number is perfect"""
def Check_Perfect(No):
    Sum = 0
    for i in range(1,No):
        if(No % i == 0):
            Sum = Sum + i   

    if(Sum == No):
        return True
    else:
        return False


"""Main function to get user input and call the check function"""
def main():
    Value = int(input("Enter the Number : "))

    Ret = Check_Perfect(Value)
    if(Ret == True):
        print(f"{Value} is Perfect Number")
    else:
        print(f"{Value} is not Perfect Number")


""" Special variable __name__ check """
if __name__ == "__main__":
    main()