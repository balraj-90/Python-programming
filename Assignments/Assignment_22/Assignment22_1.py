"""
Assignment 22 - Question 1

Program : Class Demo with Methods[__init__, fun, gun]{Object Oriented Programming}
Description:
    This program defines a class Demo with methods __init__, fun, and gun.

Author: Balraj Jagtap
Date: 25/01/2026
"""

"""Class Demo with Methods[__init__, fun, gun]"""
class Demo():
    Value = 10                  # Class Variable

    def __init__(self,A,B):     # Constructor
        self.No1 = A            # Instance Variable
        self.No2 = B            # Instance Variable

    def fun(self):              # Instance Method
        print("Inside fun method : ",self.No1,self.No2)

    def gun(self):              # Instance Method
        print("Inside gun method : ",self.No1,self.No2)


"""Main function to create objects and call methods"""
def main():
    obj1 = Demo(11,21)              
    obj2 = Demo(51,101)             

    obj1.fun()
    obj2.fun()

    obj1.gun()
    obj2.gun()


""" Special variable __name__ check """
if __name__ == "__main__":
    main()