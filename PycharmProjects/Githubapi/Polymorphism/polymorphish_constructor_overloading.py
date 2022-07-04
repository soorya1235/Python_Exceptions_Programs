class B:
    def __init__(self):
        print("Parent class constructor")

class A(B):
    def __init__(self):
        super().__init__()
        print("A class Constructor")

obj1 = A()

"""
If we just call method,with the commented code,it will print
A class contructor,if we want b class construtor to be printed
use super.__init__() which is commented.

we will get ouput like below
Parent class constructor
A class Constructor
"""

