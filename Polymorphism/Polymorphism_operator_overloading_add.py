""""
Operator overloading
Methold overloading/overiding
construtor overloading/overiding.
"""

class addoverloading():

    def __init__(self,pages):
        self.pages = pages

    def __add__(self, other):
        totalpages = self.pages - other.pages
        return totalpages


o1 = addoverloading(30)
o2 = addoverloading(20)
print(o1 + o2)

""""
Now we have + as - in the __add__ funtion.

"""