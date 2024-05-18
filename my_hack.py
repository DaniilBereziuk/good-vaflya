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

    def golovna(self):
        self.code = f'{self.num1}{self.num2}{self.num3}{self.num4}{self.num5}{self.num6}{self.num7}{self.num8}{self.num9}'
        while self.code != self.password:
            self.num1 += 1
            self.code = f'{self.num1}{self.num2}{self.num3}{self.num4}{self.num5}{self.num6}{self.num7}{self.num8}{self.num9}'
            self.num1 += 1
            if self.num1 == 10:
                self.num1 = 10
                self.num2 += 1
            if self.num2 == 10:
                self.num2 = 10
                self.num3 += 1
            if self.num3 == 10:
                self.num3 = 10
                self.num4 += 1
            if self.num4 == 10:
                self.num4 = 10
                self.num5 += 1
            if self.num5 == 10:
                self.num5 = 10
                self.num6 += 1
            if self.num6 == 10:
                self.num6 = 10
                self.num7 += 1
            if self.num7 == 10:
                self.num7 = 10
                self.num8 += 1
            if self.num8 == 10:
                self.num8 = 10
                self.num9 += 1
        print(self.code)




xz = Hacker(password="200000000")
xz.golovna()