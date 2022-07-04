class test:

    engines = 10

    def __init__(self,aa,bb):
        self.a = aa
        self.b = bb

obj = test(10,22)
print(obj.a,obj.b)

# Now we want to print class vriables
print(test.engines)

test.engines = 40

obj2 = test(20,40)
print(test.engines)

