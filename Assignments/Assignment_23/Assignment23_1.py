"""
Assignment 23 - Question 1

Program: Book Store
Description:
    This program defines a class 'BookStore' with a class variable
    to keep track of the total number of books created.

Author: Balraj Jagtap
Date: 27/01/2026
"""


class BookStore:
    """Class to represent books in a store"""

    no_of_books = 0     # Class variable

    def __init__(self, name, author):
        """Constructor to initialize book details"""
        self.name = name
        self.author = author
        BookStore.no_of_books += 1

    def display(self):
        """Display book information"""
        print(
            f"{self.name} by {self.author} | "
            f"No. of Books: {BookStore.no_of_books}"
        )


def main():
    obj1 = BookStore("Linux System Programming", "Robert Love")
    obj1.display()

    obj2 = BookStore("C Programming", "Dennis Ritchie")
    obj2.display()


if __name__ == "__main__":
    main()
