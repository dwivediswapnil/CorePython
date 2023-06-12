class PlayerCharacter:
    # constructor method
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("Runnn")


player1 = PlayerCharacter("Cindy",23)
player1.attack = 100
player2 = PlayerCharacter("Swapnil",12)

print(player1.name, player1.age,player1.run())
print(player2.name, player1.age)
print(player1.attack)