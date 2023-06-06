# class PlayerCharacter:
#   membership = True

#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def shout(self):
#     print(f'my name is {self.name}')

#   @classmethod
#   def adding_things(cls, num1, num2):
#     return num1 + num2


# # player1 = PlayerCharacter("Ron", 23)
# # player1.shout()
# #can be called using class name
# print(PlayerCharacter.adding_things(2, 4))
# ##################################################
class PlayerCharacter:
  membership = True

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def shout(self):
    print(f'my name is {self.name}')

  @classmethod
  def adding_things(cls, num1, num2):
    return cls('Teddy', num1 + num2)

  # When using static method annotation , we don't care about init attributes and maybe we want to modify them.
  @staticmethod
  def adding_things2(num1, num2):
    return (num1 + num2)


# We have a whole new player here that wa screated using cls method .
player3 = PlayerCharacter.adding_things2(2, 4)
print(player3.age)