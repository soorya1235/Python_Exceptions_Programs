class A:

    def __init__(self):
        print("Contructor of A called")

    def display(self):
        print("Instance Methold of class A")

    @classmethod
    def classmethold(cls):
        print("This is class methold")


obj = A()
print(obj.display())
#print(obj.classmethold())
print(A.classmethold())
"""
If you see the above example,we have defined the class method using the cls paramter,but we are able to access it 
using the obj...we cannot access using lie A.Clssmethold we will get error like
Type Error A.clssmethold() missing 1 required positional argument : 'cls'
to resolve this error we need to use @classmethold decorator

"""