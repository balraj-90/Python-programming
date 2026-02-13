"""
Assignment 29 - Question 4

Program: File Comparison Operations
Description:
    This program prompts the user to enter 2 file names using command line arguments and compare the contents of the both the files.
    If both the files exists, it compares the content of both files and notifies whether they are identical or different; otherwise, it notifies the user that one or both files do not exist.

Author: Balraj Jagtap
Date: 03/02/2026
"""

"""
    Importing the os module to interact with the operating system for file existence checking.
    Importing the sys module to handle command line arguments.
"""
import os
import sys

"""Main function to execute the file existence check and compare contents."""
def main():
    FileName1 = sys.argv[1]
    FileName2 = sys.argv[2]

    if os.path.exists(FileName1) and os.path.exists(FileName2):
        print(f"Both files '{FileName1}' and '{FileName2}' exist in the current directory.")    
        
        with open(FileName1, "r") as file1:
            content1 = file1.read()

        with open(FileName2, "r") as file2:
            content2 = file2.read()

        if content1 == content2:
            print("The contents of both files are identical.")
        else:
            print("The contents of the files are different.")        
        

    else:
        print(f"File '{FileName1}' or '{FileName2}' does not exist in the current directory.")    

    
"""Entry point of the program."""
if __name__ == "__main__":
    main()