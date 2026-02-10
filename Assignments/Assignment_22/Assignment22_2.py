"""
Assignment 22 - Question 2

Program : Class Circle with Methods[__init__, Accept, CalculateArea, CalculateCircumference, Display]{Object Oriented Programming}
Description:
    This program defines a class Circle with methods __init__, Accept, CalculateArea, CalculateCircumference, and Display.

Author: Balraj Jagtap
Date: 25/01/2026
"""


"""Class Circle with Methods[__init__, Accept, CalculateArea, CalculateCircumference, Display]"""
class Circle():
    PI = 3.14               # Class Variable

    def __init__ (self,Radius,Area,Circumference):                  # Constructor
        self.Radius = Radius                    # Instance Variable
        self.Area = Area                        # Instance Variable
        self.Circumference = Circumference      # Instance Variable

    def Accept(self):                   # Instance Method
        self.Radius = float(input("Enter the radius of circle : "))

    def CalculateArea(self):            # Instance Method
        Area = Circle.PI * self.Radius * self.Radius
        return Area
    
    def CalculateCircumference(self):   # Instance Method
        Circumferance = 2 * Circle.PI * self.Radius
        return Circumferance

    def Display(self):                  # Instance Method
        print("Radius of Circle is : ",self.Radius)
        print("Area of Circle is : ",self.Area)
        print("Circumference of Circle is : ",self.Circumference)


"""Main function to create object and call methods"""
def main():
    obj = Circle(0,0,0)
    obj.Accept()
    obj.Area = obj.CalculateArea()
    obj.Circumference = obj.CalculateCircumference()
    obj.Display()


""" Special variable __name__ check """
if __name__ == "__main__":
    main()