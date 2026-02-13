"""
Assignment 29 - Question 5

Program: File String Frequency Counter
Description:
    This program prompts the user to enter a file name and string using command line arguments and returns the frequency of that string in the file.
    If the file exists, it counts and prints the frequency of the specified string; otherwise, it notifies the user that the file does not exist.

Author: Balraj Jagtap
Date: 03/02/2026
"""

"""
    Importing the os module to interact with the operating system for file existence checking.
    Importing the sys module to handle command line arguments.
"""
import os
import sys

"""Main function to execute the file existence check and count string frequency."""
def main():
    FileName1 = sys.argv[1]
    String = sys.argv[2]

    if os.path.exists(FileName1):
        print("File exists in the current directory.")

        with open(FileName1, "r") as file:
            content = file.read()
            frequency = content.count(String)
            print(f"The string '{String}' appears {frequency} times in the file.")

    else:
        print(f"File '{FileName1}' does not exist in the current directory.")

    
"""Entry point of the program."""
if __name__ == "__main__":
    main()