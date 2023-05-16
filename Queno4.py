#Write a python script to update 2nd Question, add a class variable (platform) and create a classmethod to access it.
class Profile:
    name='Nagraj'
    email='babarn3333@gmail.com'
    age=24
    @classmethod
    def add_profile(cls):
        cls.platfrom='Ineuron'
        return(cls.platfrom,cls.name,cls.email,cls.age)
obj1=Profile()
print(Profile.add_profile())