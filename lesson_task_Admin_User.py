class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._level = 'user'  # Уровень доступа
        self.__personal_info = {}

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_level(self):
        return self._level

    def set_name(self, name):
        self._name = name

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._level = 'admin'

    def add_user(self, users_list, user):
        users_list.append(user)
        #print(f"Пользователь {user.get_name()} добавлен.")
        print(users_list)
# Данный метод исправлен ИИ, т.к. не работал при удалении пользователя Админом. Но его не проверяли.
    def remove_user(self, users_list, user_id):
        for user in users_list:
            if user.get_user_id() == user_id:
                users_list.remove(user)
                print(f"Пользователь с ID {user_id} удален.")
                print(users_list)
                return
        print(f"Пользователь с ID {user_id} не найден.")
users_l = []
admin = Admin('01', 'Сергей')
user1 = User('11', 'Вася')
user2 = User('12', 'Петя')

print(user1.get_name())
admin.add_user(users_l, user1)
admin.add_user(users_l, user2)

admin.remove_user(users_l,'12')

admin.remove_user(users_l,'100')