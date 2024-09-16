class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'  # Уровень доступа
        self.__personal_info = {}

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def set__personal_info(self, year, job_title, department):
        self.__personal_info = {
            'год рождения': year,
            'должность': job_title,
            'отдел': department
        }
        print(f'{self._name}, Ваша информация добавлена')

    def get__personal_info(self):
        print(f'\nМоя личная информация ({self._name}): ')
        for k, v in self.__personal_info.items():
            print(f"{k.capitalize()}: {v}")


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'
        self._user_list = []

    def add_user(self, user):
        self._user_list.append(user)
        print(f"Пользователь {user.get_name()} добавлен.")

    def remove_user(self, user_id):
        for user in self._user_list:
            if user.get_user_id() == user_id:
                self._user_list.remove(user)  # Удаляем пользователя из списка
                print(f"\nПользователь с ID {user_id} удален.")
                return  # Выходим из функции после удаления
        print(f"Пользователь с ID {user_id} не найден.")

    def get_users(self):
        for user in self._user_list:
            print(f'{user.get_user_id()} - {user.get_name()}')

admin = Admin('01', 'Сергей')
user1 = User('11', 'Вася')
user2 = User('12', 'Петя')
user3 = User('13', 'Захар')
user4 = User('14', 'Мария')

admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)
admin.add_user(user4)

user1.set__personal_info('1990', 'Менеджер', 'Офис')
user2.set__personal_info('1967', 'Главбух', 'Бухгалтерия')
user3.set__personal_info('1981', 'Курьер', 'Доставка')
user4.set__personal_info('1996', 'Специалист', 'Бухгалтерия')

user2.get__personal_info()
admin.get_users()
admin.remove_user('12')
admin.get_users()
admin.remove_user('55')
