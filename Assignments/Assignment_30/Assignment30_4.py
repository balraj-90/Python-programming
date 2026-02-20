"""
Assignment 30 - Question 4

Program: File Copier
Description:
    This program prompts the user to enter 2 file names and copy the contents of first file to second file. 
    If the file does not exist, it displays an appropriate message.

Author: Balraj Jagtap
Date: 03/02/2026
"""


import os


"""Main function"""
def main(): 
    FileName1 = input("Enter the first file name from which contents to be copied : ")
    FileName2 = input("Enter the second file name in which contents to be copied : ")
    
    if os.path.exists(FileName1):
        with open(FileName1, "r") as file:
            content = file.read()
        
        with open(FileName2, "w") as file:
            file.write(content)
        
        print(f"Contents of '{FileName1}' have been copied to '{FileName2}'.")

    else:
        print(f"The file '{FileName1}' does not exist.")


"""Entry point of the program."""
if __name__ == "__main__":
    main()