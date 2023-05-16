# Write a python script to create a Phone class with 2 methods to print the features (calling and sms).
class Phone:
    def __init__ (self,mobile_no):
        self.moblieno=mobile_no
        A=int(input('''what you want to do?
             1) Calling
             2) SMS 
        '''))
        if A==1:
            self.calling()
        elif A==2:
            self.SMS()
        else:
            print('You Select Wroung Option')
    def calling(self):
        if len(self.moblieno)==10:
            print('Calling....',self.moblieno)
            print('Call ended')
        else:
            print('Please recheak mobile number It should be 10 digit number')
    def SMS(self):
        if len(self.moblieno)==10:
            B=input('Write your SMS here >> ')
            if len(B)>0:
             print(B,'Your SMS has sucessfully Send',sep='\n')
            else:
                print('You did not Write Anythige')
        else:
            print('Please cheak entered moblie number')
In_moblie=input('Please Enter a mobile number here:>> ')
obj1=Phone(In_moblie)



