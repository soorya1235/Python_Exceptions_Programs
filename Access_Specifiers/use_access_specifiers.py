from access_specifies import car

obj = car()
print(obj.publicvar)
print(obj._protectedvariable)
print(obj._car__privatevariable)

print(obj.publicmethod())
print(obj._protectedmethod())
print(obj._car__privatemethod())