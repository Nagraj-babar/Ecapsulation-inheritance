# Write a python script to create a Calculator class with 2 methods for adding and subtracting 2 values.
class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print (self.a + self.b)
    def sub(self):
        print (self.a - self.b)
obj1=Calculator(20,10)
obj1.add()
obj1.sub()

