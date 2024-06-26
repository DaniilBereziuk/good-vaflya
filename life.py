import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print('Time to study..')
        self.progress += 0.12
        self.gladness -= 5
    def to_sleep(self):
        print('I will sleep')
        self.gladness += 3
    def to_chill(self):
        print('Reset time')
        self.gladness += 5
        self.progress -= 0.1
    def is_alive(self):
        if self.gladness <= 0:
            print('Depression..')
            self.alive = False
        elif self.progress < - 0.5:
            print('Failed..')
            self.alive = False
        elif self.progress > 5:
            print('Passed!')
            self.alive = False
    def end_of_day(self):
        print(f'Gladness - {self.gladness}')
        print(f'Progress - {self.progress}')
    def live(self, day):
        day = f'Day {day} of {self.name} life'
        print(f'{day:=^50}')
        cube = random.randint(1, 3)
        if cube == 1:
            self.to_study()
        elif cube == 2:
            self.to_sleep()
        elif cube == 3:
            self.to_chill()

        self.end_of_day()
        self.is_alive()

vova_Adidas = Student(name='vova_Adidas')
for day in range(1,50):
    if not vova_Adidas.alive:
        break
    vova_Adidas.live(day)