"""
Assignment 13 - Question 5

Program : Calculate Grade of Student
Description:
    This program defines a function to calculate and print the grade of a student based on their marks.

Author: Balraj Jagtap
Date: 28/01/2026
"""

"""Function to calculate and print grade based on marks"""
def Calculate_Grade(Marks):
    if Marks >= 75:
        print("Grade : Distinction")
    elif Marks >= 60:
        print("Grade : First Class")
    elif Marks >= 50:
        print("Grade : Second Class")
    elif Marks >= 40:
        print("Grade : Pass")
    else:
        print("Grade : Fail")


"""Main function to get user input and call the grade calculation function"""
def main():
    Marks = float(input("Enter the Marks Obtained by the Student : "))

    Calculate_Grade(Marks)


""" Special variable __name__ check """
if __name__ == "__main__":
    main()