class User:
    def sign_in(self):
        print('logged in')


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
wiz.sign_in()
wiz.attack()

arc = Archer('Sara', 20)
arc.sign_in()
arc.attack()

print(isinstance(wiz, Wizard))  # True (wiz is the instance of Wizard class)
print(isinstance(wiz, User))  # True
print(isinstance(wiz, object))  # True
print(isinstance(wiz, Archer))  # False
