"""
Assignment 13 - Question 1

Program: Calculate Area of Rectangle
Description:
    This program defines a function to calculate the area of a rectangle.

Author: Balraj Jagtap
Date: 27/01/2026
"""


"""Function to calculate area of rectangle"""
def Calculate_Area(Length, Width):
    Area = Length * Width
    
    return Area


"""Main function to get user input and call the area calculation function"""
def main():
    Value1 = int(input("Enter the Length of Rectangle : "))

    Value2 = int(input("Enter the Width of Rectangle : "))

    Ret = Calculate_Area(Value1, Value2)

    print("Area of Rectangle is : ",Ret)


""" Special variable __name__ check """
if __name__ == "__main__":
    main()