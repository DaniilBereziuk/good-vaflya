class Human:

    heigth = 170
    gladness = 10


class Student(Human):
    gladness = 0

class Worker(Human):
    gladness = 100

nick = Student()
ann = Worker()
print(f'student - {nick.heigth}, {nick.gladness}')
print(f'worker - {ann.heigth}, {ann.gladness}')

class GrandParent:
    heigth = 170
    age = 60
    gladness = 100

class Parent(GrandParent):
    age = 40

class Child(Parent):
    heigth = 110
    age = 10

    def __init__(self):
        print(self.age)
        print(self.heigth)
        print(self.gladness)

nick = Child()

class Wow:

    def _hello(self):
        print('Hello')
    def __wow(self):
        print('Wow')

x = Wow()
x._hello()
x._Wow__wow()

class A:
    hello = 'Hello'
    _hello = '_Hello'
    __hello = '__Hello'

    def __init__(self):
        self.world = 'world'
        self._world = '_world'
        self.__world = '__world'

    def printer(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)

class B(A):

    def printer_2(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)

# B().printer_2()

class Hello:

    def __init__(self):
        print('Hello')

    def not_hello(self):
        print('NOT')

class World(Hello):

    def __init__(self):
        super().__init__()
        super().not_hello()
        print('World')

World()



class Computer:

    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.memory = 128
        self.model = model

    def calculate(self):
        print('Calculating..')

class Display:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resolution = '4k'

    def display(self):
        print('I display the image on the screen..')


class SmartPhone(Computer, Display):

    def print_info(self):
        print(self.model)
        print(self.memory)
        print(self.resolution)

phone = SmartPhone(model='Iphone 14 pro max')
phone.print_info()