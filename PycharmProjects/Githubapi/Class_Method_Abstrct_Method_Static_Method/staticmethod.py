class A:

    legs = 10
    def __init__(self,a,b):
        print("Contructor of A called")
        self.a = a
        self.b = b

    def display(self):
        print("Instance Methold of class A")
        print(self.a)
        print(self.b)


    @classmethod
    def getlegscount(cls):
        print(cls.legs)
        #print(cls.a)  Note : we cannot access like this instance variables.


    @staticmethod
    def static_function():
        print("This is static methold")



obj = A(10,20)
obj.display()
A.getlegscount()
obj.static_function()

A.static_function()

"""
Note static function can be accessed using obj and clss
"""
