class PlayerCharacter:
    membership = True

    def __init__(self, name='anonymous', age=0):
        if age > 18:  # if age is less than 18 it won't initialise name and age, it will throw error
            self.name = name  # attributes
            self.age = age

    def shout(self):
        print(f'my name issss {self.name}')


player = PlayerCharacter('Bredlin', 27)
player.shout()
