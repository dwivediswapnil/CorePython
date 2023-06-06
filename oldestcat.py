# 1 Instantiate the Cat object with 3 cats
# 2 Create a function that finds the oldest cat
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
class Cat:
  
  species = 'mammal'

  def __init__(self, name, age):
    self.name = name
    self.age = age


cat1 = Cat("Mis", 3)
cat2 = Cat("Bis", 4)
cat3 = Cat("Lis", 6)

def oldest_cat(cat1, cat2, cat3):
  return max(cat1.age, cat2.age, cat3.age)


print(f'The oldest cat is {oldest_cat(cat1,cat2,cat3)} years old.')