class User:
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows of {self.num_arrows}')


wiz = Wizard('Bredlin', 500)
arc = Archer('Sara', 20)

def player_attack(char):
    char.attack()

player_attack(wiz)
player_attack(arc)

for char in [wiz, arc]:
    char.attack()