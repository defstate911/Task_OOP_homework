# Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами.
# Программа должна быть спроектирована таким образом, чтобы легко можно было добавлять новые типы оружия,
# не изменяя существующий код бойцов или механизм боя.
#
# Исходные данные:
#
# Есть класс Fighter, представляющий бойца.
# Есть класс Monster, представляющий монстра.
# Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.
#
# Шаг 1: Создайте абстрактный класс для оружия
# Создайте абстрактный класс Weapon, который будет содержать абстрактный метод attack().
#
# Шаг 2: Реализуйте конкретные типы оружия
# Создайте несколько классов, унаследованных от Weapon, например, Sword и Bow.
# Каждый из этих классов реализует метод attack() своим уникальным способом.
#
# Шаг 3: Модифицируйте класс Fighter
# Добавьте в класс Fighter поле, которое будет хранить объект класса Weapon.
# Добавьте метод change_weapon(), который позволяет изменить оружие бойца.
#
# Шаг 4: Реализация боя
# Реализуйте простой механизм для демонстрации боя между бойцом и монстром, исходя из выбранного оружия.
# Требования к заданию:
#
# Код должен быть написан на Python.
# Программа должна демонстрировать применение принципа открытости/закрытости: новые типы оружия можно легко добавлять, не изменяя существующие классы бойцов и механизм боя.
# Программа должна выводить результат боя в консоль.
# Пример результата:
#
# Боец выбирает меч.
# Боец наносит удар мечом.
# Монстр побежден!
# Боец выбирает лук.
# Боец наносит удар из лука.
# Монстр побежден!

from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return 'Боец стреляет из  лука'

class Bow(Weapon):
    def attack(self):
        return 'Боец сражается мечом'

class Fighter:
    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon  # Оружие бойца

    def attack(self):
        attack_message = self.weapon.attack()
        print(f"{self.name} наступает! {attack_message}")

    def change_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon
        print(f"{self.name} сменил оружие на {new_weapon.__class__.__name__}.")

class Monster:
    def __init__(self, name):
        self.name = name

    def defend(self):
        print(f"{self.name} защищается от атаки!")

def battle(fighter: Fighter, monster: Monster):
    print(f"\n{fighter.name} атакует {monster.name}!")
    fighter.attack()
    monster.defend()
    print(f"{monster.name} получил удар!")


sword = Sword()
bow = Bow()
fighter = Fighter('Алекс', sword)
monster = Monster('Бальтазар')

battle(fighter, monster)
fighter.change_weapon(Bow())
battle(fighter, monster)
print(f"Монстр {monster.name} побежден!")
