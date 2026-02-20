"""
Assignment 30 - Question 2

Program: Word Counter
Description:
    This program prompts the user to enter a file name and count total no. of words present in that file. 
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
            
            word_count = 0
            for line in file:
                words = line.split()
                word_count += len(words)
            
        print(f"The file '{FileName}' has {word_count} words.")
    
    else:
        print(f"The file '{FileName}' does not exist.")


    
"""Entry point of the program."""
if __name__ == "__main__":
    main()