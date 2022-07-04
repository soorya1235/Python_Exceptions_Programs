class B:

    def display(self):
        print("This is Class B display methold ")

class A(B):

   def display(self):
       #super().display()
       print("This is Class A display Method")


obj1 = A()
print(obj1.display())

"""
Note if we print it above,it will print the out as "Class A display method..to achieve overloading we 
need to call using super.like below
super.display()..it will class Class B display method first then Class A Method.
"""
