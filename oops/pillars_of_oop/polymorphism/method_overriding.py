class A:
    def show(self):
        print("in A show")

class B(A):
    def show(self):
        print("in B show")


obj = B()
obj.show()  # in B show
