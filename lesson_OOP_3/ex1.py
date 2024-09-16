# Композиция
class Engine:
    def start(self):
        print('Двигатель запущен')

    def stop(self):
        print('Двигатель остановлен')

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()

my_Car = Car()
my_Car.start()
my_Car.stop()

print()
# Агрегация
class Teacher:
    def teach(self):
        print ('преподаватель учит')

class School:
    def __init__(self, new_teacher):
        self.teacher = new_teacher

    def start_lesson(self):
        self.teacher.teach()

my_teacher = Teacher()
my_school = School(my_teacher)
my_teacher.teach()

print()

class Dog:
    def speak(self):
        return 'Woof!'

class Cat:
    def speak(self):
        return 'Meow!'

def animal_speak(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()
animal_speak(dog)
animal_speak(cat)