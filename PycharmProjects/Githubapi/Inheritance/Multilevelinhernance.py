class A():

    def hello(self):
        print("class A hello")

class B(A):

    def hello(self):
        print("class b hello")

class c(B):
    def display(self):
        print("Class c display method.")

cobj = c()
cobj.hello()

"""
Here we have followed multilevel inheritance where we have inherited Class B from Class A and Class C from B.
so when ever we call methold hello,it will call the method from the one which is loaded last
here in this case..it will print "class b hello" as we are calling cobj.hello().

"""
