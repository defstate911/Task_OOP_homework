# Создайте класс Animal с методом make_sound(). Затем создайте
# несколько дочерних классов (например, Dog, Cat, Cow), которые
# наследуют Animal, но изменяют его поведение (метод make_sound()).
# В конце создайте список содержащий экземпляры этих животных
# и вызовите make_sound() для каждого животного в цикле.

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def make_sound(animal):
#         print(animal.make_sound())
#
# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def make_sound(self):
#         return f'Гав! -  сказал пёс {self.name}'
#
# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def make_sound(self ):
#         return f'Mяу - сказал кот {self.name}'
#
# class Cow(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def make_sound(self):
#         return f'Му-у - сказала корова {self.name}'
# animals = [Cat('Васька'), Dog('Шарик'), Cow('Буренка'), Cat('Пушистик')]
# # cat1 = Cat('Васька')
# # cat2 = Cat('Пушистик')
# # dog1 = Dog('Шарик')
# # cow1 = Cow('Буренка')
#
# # print(cat1.make_sound())
# # print(cat2.make_sound())
# # print(dog1.make_sound())
# # print(cow1.make_sound())
#
# animals = [Cat('Васька'), Dog('Шарик'), Cow('Буренка'), Cat('Пушистик')]
# for animal in animals:
#     print(animal.make_sound())