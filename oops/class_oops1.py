class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name  # attributes
        self.age = age

    def run(self):
        print('running')


player1 = PlayerCharacter('Cindy', 44)
print(player1)  # <__main__.PlayerCharacter object at 0x000001E5CF5C8140>
print(player1.name, player1.age)  # Cindy

player2 = PlayerCharacter('Tom', 21)
print(player2.name)  # Tom
player2.run()

player2.attack = 50
print(player2.attack)

class PlayerChar:
    membership = True  # class object attribute
    def __init__(self, name, age):
        if PlayerChar.membership:
            self.name = name  # attributes
            self.age = age

    def shout(self):
        print(f'my name isssss {self.name}')

play = PlayerChar('Bredlin', 27)
play.shout()
