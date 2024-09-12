class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def adding_product(self, name, price):
        self.items[name] = price

    def removal_product(self, name):
        self.items.pop(name)
        print(f'\n{name} - этот товар отсутствует в магазине')

    def getting_price(self, name):
        if name not in self.items.keys():
            print(None)
        else:
            print(f'\n{name} стоят {self.items[name]} руб')

    def update_price(self, name, price):
        self.items.update({name: price})

    def show_info(self):
        print(f'\nМагазин "{self.name}"')
        print(f'Находится по адресу:  {self.address}')
        print(f'\nВ наличии: ')
        print(*list(self.items.keys()), sep=', ')
        print(f'\nПрайс: ')
        #print(*(list(self.items.items())), sep='\n')
        [print(f'{k} - {v} руб') for k,v in self.items.items()]

store_1 = Store('Овощи-фрукты', 'г. Солнечный, ул. Весенняя, д. 8' )
store_2 = Store('Хозяйственный', 'г. Солнечный, ул. Осенняя, д. 1' )
store_3 = Store('Цветы', 'г. Солнечный, ул. Ромашковая, д. 109' )

store_1.adding_product('яблоки', 2)
store_1.adding_product('бананы', 1.5)
store_1.adding_product('морковь', 0.5)
store_1.adding_product('картофель', 1)

store_2.adding_product('ножницы', 1)
store_2.adding_product('молоток', 5)
store_2.adding_product('дрель', 50)
store_2.adding_product('корзина', 10)

store_3.adding_product('Цикламен', 200)
store_3.adding_product('Хризантемы', 80)
store_3.adding_product('Розы', 150)
store_3.adding_product('Тюльпаны', 100)
store_3.adding_product('Гвоздики', 70)

store_1.show_info()
store_2.show_info()

store_2.removal_product('корзина')
store_2.show_info()

store_1.getting_price('бананы')

store_1.update_price('бананы', 2)

store_3.removal_product('Гвоздики')

store_1.show_info()
store_3.show_info()

store_3.getting_price('Гвоздики')