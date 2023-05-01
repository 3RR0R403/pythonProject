import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 3000
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.2
        self.gladness -= 3
        self.money -= 100


    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3
        self.progress -= 0.05

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.15
        self.money -= 250

    def to_work(self):
        print("Work time")
        self.money += 300
        self.gladness -= 2
        self.progress += 0.05

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress > 10:
            print("Passed externally…")
            self.alive = False
        elif self.money <= 0:
            print("Poor…")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money = {self.money}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if self.progress < 0.1 and self.gladness > 3 or live_cube == 1:
            self.to_study()
        elif self.gladness < 10 or live_cube == 2:
            self.to_sleep()
        elif self.gladness < 3 and self.progress > 0.2 and self.money > 1000 or live_cube == 3:
            self.to_chill()
        elif self.money < 300 and self.gladness > 3 or live_cube == 4:
            self.to_work()
        self.end_of_day()
        self.is_alive()

nick = Student(name="Nick")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)