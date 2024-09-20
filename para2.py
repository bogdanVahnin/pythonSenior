import random


class Student:
    def __init__(self, name):
        self.name = name
        self.progress = 0
        self.gladness = 50
        self.alive = True

    def to_study(self):
        print("Я навчаюсь")
        self.progress += 0.1
        self.gladness -= 5

    def it_school(self):
        print("Я в школі")
        self.progress += 0.1
        self.gladness -= 5

    def to_sleep(self):
        print("Я пішов спати")
        self.progress += 0.02
        self.gladness += 5

    def to_chill(self):
        print("Я відпочіваю")
        self.gladness += 5
        self.progress -= 0.1

    def to_walkStreet(self):
        print("Я гуляю на вулиці")
        self.gladness += 5
        self.progress -= 0.1

    def to_playComp(self):
        print("Я граю в комп'ютер")
        self.gladness += 8
        self.progress -= 0.5
        self.skikiGravVPK += 1

    def info(self):
        print(f"Рівень навчання {round(self.progress, 2)}")
        print(f"Задоволення {self.gladness}")

    def is_alive(self):
        if self.progress > 10:
            print("Ми все вивчили і закінчили МКА ШАГ")
            self.alive = False
        if self.progress < -0.5:
            print("Ми втратили інтерес до навчання...")
            self.alive = False
        if self.gladness <= 0:
            print("У мене дипресія")
            self.alive = False

    def live(self, day):
        print(f"День {day} з життя {self.name}")
        print("================================")
        choice = random.randint(1, 5)
        print(choice)
        if choice == 1:
            self.to_study()
        elif choice == 2:
            self.to_sleep()
        elif choice == 3:
            self.it_school()
        elif choice == 4:
            self.to_walkStreet()
        elif choice == 5:
            choice = random.randint(1, 10)
            if choice == 10:
                self.to_playComp()



        self.info()
        self.is_alive()



student = Student('C2121')
'''student.info()
student.to_study()
student.info()
student.to_chill()
student.info()'''

for day in range(365):
    if student.alive == False:
        break
    student.live(day)














