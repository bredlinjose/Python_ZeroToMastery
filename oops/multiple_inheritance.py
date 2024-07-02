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

    def check_arrows(self):
        print(f'arrows remaining {self.num_arrows}')

    def run(self):
        print('runs really fast')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, num_arrows):
        Archer.__init__(self, name, num_arrows)
        Wizard.__init__(self, name, power)


hb = HybridBorg('borgie', 50, 100)
hb.sign_in()
hb.attack()
hb.check_arrows()
hb.run()
