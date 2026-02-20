"""
Assignment 30 - Question 1

Program: Line Counter
Description:
    This program prompts the user to enter a file name and count how many lines are present in that file. 
    If the file does not exist, it displays an appropriate message.

Author: Balraj Jagtap
Date: 03/02/2026
"""


import os

"""Main function to execute the file existence check."""
def main(): 
    FileName = input("Enter the file name : ")
    
    if os.path.exists(FileName):
        
        with open(FileName,"r")as file:
            
            line_count = 0
            for line in file:
                line_count += 1

        print(f"The file '{FileName}' has {line_count} lines.")
    
    else:
        print(f"The file '{FileName}' does not exist.")


    
"""Entry point of the program."""
if __name__ == "__main__":
    main()