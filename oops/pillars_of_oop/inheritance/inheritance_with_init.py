class A:
    def __init__(self):
        print('In A init')

    def feature1(self):
        print('Feature 1 is working')

    def feature2(self):
        print('Feature 2 is working')


class B(A):
    def __init__(self):
        # super().__init__()  # this will execute the init of A
        print('In B init')

    def feature3(self):
        print('Feature 3 is working')

    def feature4(self):
        print('Feature 4 is working')


obj = B()  # this will print only the B init, If B init is not there then it will print the A init
