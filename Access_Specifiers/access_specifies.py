""""
3 type of access specifies
public,prrivate,protected
"""

class car:

    def __init__(self):
        print("Constructor called")

    publicvar = 10
    _protectedvariable = 20
    __privatevariable = 30

    def publicmethod(self):
        print("Accessing public method")

    def _protectedmethod(self):
        print("protected method")

    def __privatemethod(self):
        print("private method")