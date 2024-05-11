from colorama import Fore


password = "ga7cz129pq"

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
num6 = 6
num7 = 7
num8 = 8
num9 = 9
num10 = 10

class Hacker:
    def __init__(self, password):
        self.num1 = 0
        self.num2 = 0
        self.num3 = 0
        self.num4 = 0
        self.num5 = 0
        self.num6 = 0
        self.num7 = 0
        self.num8 = 0
        self.num9 = 0
        self.password = password

    def num_1(self):
        self.num1 += 1
        self.code = f'{self.num1}{self.num2}{self.num3}{self.num4}{self.num5}{self.num6}{self.num7}{self.num8}{self.num9}'
        print(self.code)


xz = Hacker(password="2k0fw10geq")
xz.num_1()