"""
Assignment 30 - Question 3

Program: Word Counter
Description:
    This program prompts the user to enter a file name and display the contents of file line by line. 
    If the file does not exist, it displays an appropriate message.

Author: Balraj Jagtap
Date: 03/02/2026
"""


import os


"""Main function"""
def main(): 
    FileName = input("Enter the file name : ")
    
    if os.path.exists(FileName):
        
        with open(FileName,"r")as file:
            print("File Contents are : ")    
            
            for line in file:
                print(line)

    
    else:
        print(f"The file '{FileName}' does not exist.")


    
"""Entry point of the program."""
if __name__ == "__main__":
    main()