# Write a python script to update 2nd Question, change email and age to __email and __age.
class Profile:
    name='nagraj'
    email='babarn3333@gmail.com'
    age=20
    def set_update_profile(cls):
        cls.__email='babarn3333@gmail.com'
        cls.__age=24
        return cls.__email,cls.__age
obj1=Profile()
print(obj1.set_update_profile())