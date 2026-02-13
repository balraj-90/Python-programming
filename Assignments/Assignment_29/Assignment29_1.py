"""
Assignment 29 - Question 1

Program: File Existence Checker
Description:
    This program prompts the user to enter a file name and checks if the file exists in the current directory.
    If the file exists, it prints a confirmation message; otherwise, it notifies the user that the file does not exist.

Author: Balraj Jagtap
Date: 03/02/2026
"""

"""
    Importing the os module to interact with the operating system for file existence checking.
"""
import os

"""Main function to execute the file existence check."""
def main():
    FileName = input("Enter File Name : ")

    if os.path.exists(FileName):
        print(f"File '{FileName}' exists in the current directory.")    
    else:
        print(f"File '{FileName}' does not exist in the current directory.")    

    
"""Entry point of the program."""
if __name__ == "__main__":
    main()