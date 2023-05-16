'''Write a python script to add the new method in SmartPhone class which accepts
Truecaller object as a parameter and call the fetch method of Truecaller.'''
class Truecaller():
    def __init__(self):
        self.dict1={8999467024:'Nagraj',1234567893:'Ramesh',8999283543:'suresh'}
class SmartPhone(Truecaller):
    def new_fectch(self):
        self.fetch()
class Truecaller(SmartPhone):
   def fetch(self):
        print(self.dict1)
obj1=Truecaller()
obj1.new_fectch()
