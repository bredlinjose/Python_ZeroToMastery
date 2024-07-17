class A:
    def feature1(self):
        print('Feature 1 is working')

    def feature2(self):
        print('Feature 2 is working')

class B(A):  # single inheritance
    def feature3(self):
        print('Feature 3 is working')

    def feature4(self):
        print('Feature 4 is working')

class C(B):  # multilevel inheritance
    def feature5(self):
        print('Feature 5 is working')


objA = A()
objA.feature1()
objA.feature2()

objB = B()
objB.feature1()
objB.feature2()
objB.feature3()
objB.feature4()

objC = C()
objC.feature1()
objC.feature2()
objC.feature3()
objC.feature4()
objC.feature5()
