class PyCharm:

    def execute(self):
        print('Compiling')
        print('Running')

class MyEditor:

    def execute(self):
        print('Spell Check')
        print('Convention Check')
        print('Compiling')
        print('Running')


class Laptop:

    def code(self, ide):
        ide.execute()


ide1 = PyCharm()
ide2 = MyEditor()

lap1 = Laptop()
lap1.code(ide1)
lap1.code(ide2)

