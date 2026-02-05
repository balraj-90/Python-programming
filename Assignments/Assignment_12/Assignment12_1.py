"""
Assignment 12 - Question 1

Program: Vowel or Consonant
Description:
    This program defines a function to check if a character is a vowel or consonant.

Author: Balraj Jagtap
Date: 27/01/2026
"""


"""Function to check if character is vowel or consonant"""
def is_vowel_or_consonant(char):
    vowels = "aeiouAEIOU"
    if char in vowels:
        print("It is a vowel.")
    else:
        print("It is a consonant.")


"""Main function to get user input and call the check function"""
def main():
    char = input("Enter the Character : ")
    if len(char) != 1 or not char.isalpha():
        print("Please enter a single alphabetic character.")
        return

    is_vowel_or_consonant(char)                 


if __name__ == "__main__":
    main()