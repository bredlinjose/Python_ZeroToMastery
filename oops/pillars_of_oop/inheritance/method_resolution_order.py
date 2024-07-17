#  MRO - Method Resolution Order
class A:
    def __init__(self):
        print('In A init')

    def feature1(self):
        print('Feature 1-A is working')

class B:
    def __init__(self):
        print('In B init')

    def feature1(self):
        print('Feature 1-B is working')

    def feature2(self):
        print('Feature 2 is working')

class C(A, B):
    def __init__(self):
        super().__init__()
        print('In C init')

    def feat(self):
        super().feature2()
        super().feature1()


print(C.mro())  # [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

# whenever you have multiple inheritance it will start from left to right (A-- left, B-- right)
obj = C()  # In A init  In C init
obj.feature1()  # Feature 1-A is working

obj.feat()
