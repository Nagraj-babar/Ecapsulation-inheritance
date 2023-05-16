'''Write a python script to create an application like Truecaller where names and
numbers are stored. Truecaller class will have 2 methods (1st to fetch the name of a
number and 2nd to add a new entry).'''
class Truecaller():
    def __init__(self,mobile):
        self.dict1={8999467024:'Nagraj',1234567893:'Ramesh',8999283543:'suresh'}
        self.mobile=mobile
        self.trueid()
    def trueid(self):
        if self.mobile in self.dict1.keys():
            print(self.dict1[self.mobile],'is calling')
        else:
            print('Name is not in database')
            self.fetch()
    def fetch(self):
        self.name=input('please enter the name: ')
        self.dict1.update({self.mobile:self.name})
        print(self.dict1,'This Numeber is sucessfully updated',sep='\n')
caller_no=int(input('Enter the number: '))
obj1=Truecaller(caller_no)
    