class Car:
    def __init__(self, make, model):
        self.public_make = make # Открытый атрибут
        self._protected_model = model # Защищенный атрибут
        self.__private_year = 2022 # Приватный атрибут

    def public_method(self ):
        return f'Это открытый метод. Машина: {self.public_make} {self._protected_model}.'

    def _protected_metod(self):
        return f'Это защищенный метод'

    def __private_metod(self):
        return f'Это приватный метод'

class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size

    def get_details(self):
        # Можно обратиться к открытому и защищенному атрибуту, но не к приватному
        details = f'{self.public_make} {self._protected_model}, батарея: {self.battery_size} KWh'
        # нельзя напрямую обратиться к  __private_metod и __private_year
        return details

# Создание экземпляра ElectricCar
tesla = ElectricCar('Tesla', 'Model S', 100)

# Доступ к открытому атрибуту и методу
print(tesla.public_make)
print(tesla.public_method())

# Доступ к защищенному атрибуту (не рекомендуется, но возможно)
print(tesla._protected_model)
print(tesla._protected_metod())

# Доступ к приватному атрибуту и методу не возможен, но Питон позволяет обойти это ограничение (не рекомендуется)
#print(tesla.__private_year) # будет ошибка
# Для получения доступа к приватному атрибуту можно использовать mangling.
print(tesla._Car__private_year) # 2022 вывелось из-за добавления _Car

print(tesla._Car__private_metod()) # это приватный метод сработал из-за _Car