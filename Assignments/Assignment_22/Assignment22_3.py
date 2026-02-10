"""
Assignment 22 - Question 3

Program : Class Arithematic with Methods[__init__, Accept, Addition, Subtraction, Multiplication, Division]{Object Oriented Programming}
Description:
    This program defines a class Arithematic with methods __init__, Accept, Addition, Subtraction, Multiplication, and Division.

Author: Balraj Jagtap
Date: 25/01/2026
"""

"""Class Arithemetic with Methods[__init__, Accept, Addition, Subtraction, Multiplication, Division]"""
class Arithemetic():

    def __init__ (self,Value1,Value2):          # Constructor
        self.Value1 = Value1            # Instance Variable
        self.Value2 = Value2            # Instance Variable

    def Accept(self):           # Instance Method
        self.Value1 = int(input("Enter the First Number : "))
        self.Value2 = int(input("Enter the Second Number : "))

    def Addition(self):         # Instance Method
        return self.Value1 + self.Value2
    
    def Subtraction(self):      # Instance Method   
        return self.Value1 - self.Value2

    def Multiplication(self):   # Instance Method
        return self.Value1 * self.Value2

    def Division(self):         # Instance Method
        return self.Value1 / self.Value2


"""Main function to create object and call methods"""
def main():        
    obj = Arithemetic(0,0)
    obj.Accept()
    print("Addition of two numbers is : ",obj.Addition())
    print("Subtraction of two numbers is : ",obj.Subtraction())
    print("Multiplication of two numbers is : ",obj.Multiplication())
    print("Division of two numbers is : ",obj.Division())

   
""" Special variable __name__ check """
if __name__ == "__main__":
    main()

