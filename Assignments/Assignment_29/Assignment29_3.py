"""
Assignment 29 - Question 3

Program: File Copy Operations
Description:
    This program prompts the user to enter a file name using command line arguments and creates a new file named 'output.txt' that copies the contents of the input file.
    If the input file exists, it copies the content to 'output.txt'; otherwise, it notifies the user that the file does not exist.

Author: Balraj Jagtap
Date: 03/02/2026
"""

"""
    Importing the os module to interact with the operating system for file existence checking.
    Importing the sys module to handle command line arguments.    
"""
import os
import sys


"""Main function to execute the file existence check and copy content."""
def main():
    FileName = sys.argv[1]

    if os.path.exists(FileName):
        print(f"File '{FileName}' exists in the current directory.")    
        
        with open(FileName, "r") as infile:
            content = infile.read()

        with open("Output.txt", "w") as outfile:
            outfile.write(content)

        print("Content copied to 'Output.txt' successfully.")

    else:
        print(f"File '{FileName}' does not exist in the current directory.")    

    
"""Entry point of the program."""
if __name__ == "__main__":
    main()