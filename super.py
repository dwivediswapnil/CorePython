class User(object):
    def __init__(self,email):
        self.email = email
    def sign_in(self):
        print("Logged in")

class Wizard(User):
    def __init__(self,name,power,email):
        # User.__init__(self,email)
        super().__init__(email)
        self.name = name
        self.power = power        

    def attack(self):
        print(f"Attack with {self.power} ")    

wizard1 = Wizard("Merlin",60,'merlin@gmail.com')
print(wizard1.email)  

#dir method will give list of methods to which it has access to . 
print(dir(wizard1))