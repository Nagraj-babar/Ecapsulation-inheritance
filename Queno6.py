# Write a python script to create a Calculator 2.0 class with 2 methods for multiplication and division of 2 values and inherit it from the Calculator class.
class Calculator:
   def ADD(self):
            self.a=int(input('Enter a first number: '))
            self.b=int(input('Enter a secound number: '))
            self.add()
   def SUB(self):
            self.a=int(input('Enter a first number: '))
            self.b=int(input('Enter a secound number: '))
            self.sub()
   def add(self):
        print (self.a + self.b)
   def sub(self):
        print (self.a - self.b)
class Calculator_2(Calculator):
    def calculator(self):
     A=int(input('''1).press 1 for addtion 
        2).press 2 for subtraction 
        3) Press 3 for multiplication
        4) Press 4 for Divison'''))
     if A==1:
        self.ADD()
     elif A==2:
        self.SUB()
     elif A==3:
        self.mul()
     elif A==4:
        self.truediv()
    def mul(self):
         self.a=int(input('Enter a 1st number: '))
         self.b=int(input('Enter a 2nd number: '))
         print(self.a*self.b)
    def truediv(self):
         self.a=int(input('Enter a 1st number: '))
         self.b=int(input('Enter a 2nd number: '))
         print(self.a/ self.b)
obj3=Calculator_2()
obj3.calculator()

