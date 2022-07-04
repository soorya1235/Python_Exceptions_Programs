class A():

    def hello(self):
        print("class A hello")

class B():

    def hello(self):
        print("class b hello")

class c(B,A):
    def display(self):
        print("Class c display method.")

cobj = c()
cobj.hello()

"""
Here we have followed multiple inheritance where we have inherited class B and A in to Class C.
so if we call hello method,it will call class b hello methold,because we have ordered like this
c(B,A)..if we want A hello methold to be printed use (A,B)
"""
