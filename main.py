
class Student:
    print('Hi! I am a student')

    def __init__(self, height,name):
        self.name = name
        self.height = height
        print('I am alive')
    def grow(self, value=1):
        self.height += value
    def __str__(self):
        return f'I am a student. My name is {self.name}'

artem = Student(height=150, name='artem')
print(f'artem height {artem.height}')
artem.grow(30)
print(f'artem heght after grow {artem.height}')
print(artem)

danya = Student(height=160, name='danya')
print(f'danya height {danya.height}')
artem.grow(20)
print(f'danya heght after grow {danya.height}')
print(danya)