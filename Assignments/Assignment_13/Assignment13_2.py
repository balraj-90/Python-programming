"""
Assignment 13 - Question 2

Program: Calculate Area of Circle
Description:
    This program defines a function to calculate the area of a Circle.

Author: Balraj Jagtap
Date: 28/01/2026
"""


"""Function to calculate area of circle"""
def Calculate_Area(Radius):
    Area = 3.14 * Radius * Radius
    
    return Area


"""Main function to get user input and call the area calculation function"""
def main():
    Value1 = int(input("Enter the Radius of Circle : "))

    Ret = Calculate_Area(Value1)

    print("Area of Circle is : ",Ret)


""" Special variable __name__ check """
if __name__ == "__main__":
    main()