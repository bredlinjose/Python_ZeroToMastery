class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name  # attributes
        self.age = age

    def shout(self):
        print(f'my name issss {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2



player = PlayerCharacter('Bredlin', 27)
player.shout()