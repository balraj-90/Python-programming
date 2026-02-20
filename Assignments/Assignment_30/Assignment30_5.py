"""
Assignment 30 - Question 5

Program: File Word Searcher
Description:
    This program prompts the user to enter  file name and a word from user and checks whether that word is present in file or not.
    If the file does not exist, it displays an appropriate message.

Author: Balraj Jagtap
Date: 03/02/2026
"""


import os


def main(): 
    FileName = input("Enter the file name : ")
    Word = input("Enter the word to be searched in the file : ")
    
    if os.path.exists(FileName):
        with open(FileName, "r") as file:
            content = file.read()
 
            if Word in content:
                print(f"The word '{Word}' is present in the file '{FileName}'.")
            
            else:
                print(f"The word '{Word}' is not present in the file '{FileName}'.")

    else:
        print(f"The file '{FileName}' does not exist.")


if __name__ == "__main__":
    main()