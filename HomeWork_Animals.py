# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы,
# если требуется (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию
# о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper`
# и `heal_animal()` для `Veterinarian`).
#
# Дополнительно:
# Попробуйте добавить дополнительные функции в вашу программу,
# такие как сохранение информации о зоопарке в файл и возможность её загрузки,
# чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return f'{self.name} издает звук.'

    def eat(self):
        return f'{self.name} ест пищу.'

class Bird(Animal):
    def __init__(self, name, age,  voice,  color):
        super().__init__(name, age)
        self.voice = voice
        self.color = color

    def make_sound(self):
        return f'{self.voice} -  сказал  {self.name}'

    def eat(self):
        return f'Любимое блюдо у {self.name} - {self.favorite_food}'

class Mammal(Animal):
    def __init__(self, name, age,  favorite_food, voice):
        super().__init__(name, age)
        self.voice = voice
        self.favorite_food = favorite_food

    def make_sound(self):
        return f'{self.voice} -  сказал  {self.name}'

    def eat(self):
        return f'Любимое блюдо у {self.name} - {self.favorite_food}'

class Reptile(Animal):
    def __init__(self, name, age,  favorite_food):
        super().__init__(name, age)
        self.favorite_food = favorite_food

    def eat(self):
        return f'Любимое блюдо у {self.name} - {self.favorite_food}'

# def print_make_sound(animal):
#     print(animal.make_sound())

def print_eat(animal):
    print(animal.eat())

cat_1 = Mammal('Кузя', 2, 'сметана', 'Мяу-мяу')
dog_1 = Mammal('Барбос', 5, 'курочка', 'Гав-гав!')
crocodile_1 = Reptile('Гена', 46, 'рыба')

print_eat(cat_1)
print_eat(dog_1)
print_eat(crocodile_1)

animals = [cat_1, dog_1, crocodile_1]
def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

animal_sound(animals)