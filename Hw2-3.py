import random
class Cat:
    def init(self, name):
        self.name=name
        self.gladness=3
        self.hungry=1
        self.alive=True
    def to_eat(self):
        print("Час їсти!")
        self.hungry+=0.95
        self.gladness-=1
    def to_chill(self):
        print("Час відпочити!")
        self.gladness+=5
        self.hungry-=3
    def to_sleep(self):
        print("Час спати!")
        self.gladness+=3
    def is_alive(self):
        if self.hungry<-0.5:
            print("Здох від голоду...")
            self.alive=False
        elif self.gladness<=0:
            print("Дипресія...")
            self.alive=False
    def end_of_day(self):
        print(f"Gladness -{self.gladness}")
        print(f"Hungry -{round(self.hungry, 2)}")
    def live(self, day):
        day="Day" + str(day) + "of" + self.name +"life"
        print(f"{day:=^50}")
        live_cube=random.randint(1,3)
        if live_cube==1:
            self.to_eat()
        elif live_cube==2:
            self.to_sleep()
        elif live_cube==3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()
jora=Cat(name="Jora")
for day in range(365):
    if nick.alive==False:
        break
    jora.live(day)
