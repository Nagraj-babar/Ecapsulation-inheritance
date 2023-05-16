# Write a python script to update the above Profile class with encapsulation.
class Profile:
    name='nagraj'
    email='babarn3333@gmail.com'
    age=24
    @classmethod
    def update_profile(cls):
       cls.email ='visvajeet@gmail.com'
       return cls.email
obj1=Profile()
print(obj1.update_profile())