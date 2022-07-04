
try:
    a=int(input("Enter the no"))
    b=int(input("Enter the no"))
    c= a/b
except Exception as e:
    print(e.__doc__)
else:
    print("No exception occured,so lese called.")
finally:
    print("I am always exeucted...whether exception exists or not")


