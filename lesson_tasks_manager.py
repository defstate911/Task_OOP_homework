class Task:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        self.tasks.append({
                           'description': description,
                           'deadline': deadline,
                           'status': 'не выполнено',
                           })

    def complete_task(self, description):
        for task in self.tasks:
            if task['description'] == description:
                task['status'] = 'выполнено'
                print(f'\nЗадача "{description}" выполнена ')

    def show_task(self):
        print('\nТекущие задачи: ')
        for task in self.tasks:
            if task['status'] == 'не выполнено':
                print(f"{task['description']} - {task['deadline']}")


t = Task()
t.add_task('Прочитать книгу', '12.05.25')
t.add_task('Пробежать марафон', '14.05.25')
t.add_task('Починить машину', '27.05.25')

t.show_task()

t.complete_task('Прочитать книгу')

t.show_task()