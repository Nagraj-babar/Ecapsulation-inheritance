# Write a python script to create a SmartPhone class by inheriting Calculator 2.0 and Phone Class.
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
     A=int(input('''1) press 1 for ADDTION
     2) press 2 for SUBTRACTION
     3) press 3 for MULTIPLICATION
     4) press 4 for DIVISION >> '''))
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
class Phone:
    def PHONE(self):
        self.mobileno=input('Please Enter a mobile number here:>> ')
        if len(self.mobileno)==10:
            self.calling()
        else: 
            print('Recheak the moblie number')
    def message(self):
        self.moblieno=input('Enter a mobile number: ')
        if len(self.moblieno)==10:
            self.SMS()
        else:
            print('Recheak the moblie number')
    def calling(self):
            print('Calling....',self.mobileno)
            print('Call ended')
    def SMS(self):
            B=input('Write your SMS here >> ')
            if len(B)>0:
             print(B,'Your SMS has sucessfully Send',sep='\n')
            else:
                print('You did not Write Anythige')
#In_moblie=input('Please Enter a mobile number here:>> ')
class SmartPhone(Phone,Calculator_2):
    def __init__(self):
        B=int(input('''1. Press 1 to use calling
        2.press 2 for sms
        3. press 3 for calculations
        '''))
        if B==1:
            self.PHONE()
        elif B==2:
            self.message()
        elif B==3:
            self.calculator()
object1=SmartPhone()
#object1.smartphone()