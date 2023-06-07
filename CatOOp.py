class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals
    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def walk(self):
        return f'{self.name} is just walking around'

class Billoo1(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Billoo2(Cat):
    def sing(self, sounds):
        return f'{sounds}' 

#1. Add another cat
class Billoo3(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# 2 Create a list of all of the pets (create 3 cat instances
#  from the above)  
billoo1 = Billoo1('Billoo1',1)
billoo2 = Billoo2('Billoo2',2) 
billoo3 = Billoo3('Billoo3',3)

my_cats = [billoo1,billoo2,billoo3]

# 3 Instantiate the Pet class with all your cats use variable 
# my_pets
my_pets = Pets(my_cats)           
my_pets.walk()
