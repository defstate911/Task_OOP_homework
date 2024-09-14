class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self. items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар {item_name} был добавлен в {self.name}")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар {item_name} удален из {self.items}")

    def get_price(self, item_name):
            return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            old_price = self.items[item_name]
            self.items[item_name] = new_price
            print(f"Цена товара {item_name} была {old_price}, стала - {new_price}  обновлена в {self.name}")
        else:
            print(f"Товар {item_name} не найден")

store1 = Store("Пятерочка","ул. Ленина, 40")
store2 = Store("Магнит","ул. Ленина, 44")
store3 = Store("Ярче","ул. Ленина, 80")

store1.add_item('хлеб','50')
store1.add_item('Молоко','120')
store1.add_item('Гречка','70')

store1.remove_item('Хлеб')

print(store1.get_price('Молоко'))

store1.update_price('Гречка','200')

store1.update_price('Макароны','100')