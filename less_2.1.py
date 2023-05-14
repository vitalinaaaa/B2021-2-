import random
class Student:
    def __init__(self, name):
        self.name=name
        self.gladness=50
        self.progress=0
        self.money=5
        self.alive=True
    def to_study(self):
        print("Час навчатись!")
        self.progress+=0.95
        self.gladness-=3
        self.money-=1
    def to_chill(self):
        print("Час відпочити!")
        self.gladness+=5
        self.progress-=0.1
    def to_sleep(self):
        print("Час спати!")
        self.gladness+=3
    def to_work(self):
        print("Потрібно йти на роботу!")
        self.money+=5
        self.gladness-=1
    def is_alive(self):
        if self.progress<-0.5:
            print("Відраховано...")
            self.alive=False
        elif self.gladness<=0:
            print("Дипресія...")
            self.alive=False
        elif self.money<=0:
            print("Ти став бомжом")
            self.alive=False
        elif self.progress>4.10:
            print("Вітаю з степендією!")
            self.money+=10
            self.gladness+=3
        elif self.progress>=100:
            print("Закінчив екстерном")
            self.alive=False
    def end_of_day(self):
        print(f"Gladness -{self.gladness}")
        print(f"Progress -{round(self.progress, 2)}")
    def live(self, day):
        day="Day" + str(day) + "of" + self.name +"life"
        print(f"{day:=^50}")
        live_cube=random.randint(1,3)
        if live_cube==1:
            self.to_study()
        elif live_cube==2:
            self.to_sleep()
        elif live_cube==3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()
nick=Student(name="Nick")
for day in range(365):
    if nick.alive==False:
        break
    nick.live(day)
