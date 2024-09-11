class Warrior():
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f'{self.name} лег спать')
        self.endurance += 2

    def eat(self):
        print(f'{self.name} сел кушать')
        self.power += 1

    def hit(self):
        print(f'{self.name} бьет кого - то')
        self.endurance -= 6

    def walk(self):
        print(f'{self.name} гуляет')

    def info(self):
        print(f'имя воина - {self.name}')
        print(f'цвет волос воина - {self.hair_color}')
        print(f'сила воина - {self.power}')
        print(f'выносливость воина - {self.endurance}')

war1 = Warrior('Степа', 76, 54, 'Рыжий')
#print(war1)
print(war1.name)
print(war1.power)
print(war1.endurance)
print(war1.hair_color)

war2 = Warrior('Егор', 45, 23, 'Блонд')
war2.info()

print(war1.endurance)
print(war1.power)

war1.walk()
war1.hit()
war1.eat()
war1.sleep()

print(war1.endurance)
print(war1.power)

