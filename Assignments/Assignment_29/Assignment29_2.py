"""
Assignment 29 - Question 2

Program: File Existence Checker with Content Display
Description:
    This program prompts the user to enter a file name and Displays entire content of file on console.
    If the file exists, it prints the content of the file; otherwise, it notifies the user that the file does not exist.

Author: Balraj Jagtap
Date: 03/02/2026
"""

"""
    Importing the os module to interact with the operating system for file existence checking.
"""
import os

"""Main function to execute the file existence check and display content."""
def main():
    FileName = input("Enter File Name : ")

    if os.path.exists(FileName):
        print(f"File '{FileName}' exists in the current directory.")    
        
        with open(FileName, 'r') as file:
            content = file.read()
            print("Content of the file:")
            print(content)

    else:
        print(f"File '{FileName}' does not exist in the current directory.")    

    
"""Entry point of the program."""
if __name__ == "__main__":
    main()