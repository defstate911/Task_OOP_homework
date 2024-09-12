class Task:
    def __init__(self):
        self.tasks = []

    def add_task_and_date(self,  description, deadline):
        task = {"description": description, "deadline": deadline, "completed": False}
        self.tasks.append(task)
        #return f'Задача - {task.'description'}, срок исполнения - {self.release_date}'

    def mark_task_completed(self, task_description):
        for task in self.tasks:
            if task["description"] == task_description:
                task["completed"] = True
                return f"Задача '{task_description}' отмечена как выполненная."
        return f"Задача '{task_description}' не найдена."

    def display_not_completed_tasks(self):
        print("\nНевыполненные задачи:")
        for task in self.tasks:
            if not task["completed"]:
                status = "Не выполнена"
                print(f"Задача: {task['description']}, Дедлайн: {task['deadline']}, Статус: {status}")
    def all_task_date(self, date):
        print(f'\nВот список дел на дату {date}')
        tasks_found = False
        for task in self.tasks:
                if task['deadline'] == date and  not task['completed']:

                    print(f"-{task['description']}")
                    tasks_found = True  # Устанавливаем флаг, если задача найдена
        if tasks_found == False:  # Если задачи не найдены, выводим сообщение один раз
                print(f'На {date} дату задач не найдено')

task_manager = Task()
task_manager.add_task_and_date("Сделать домашнее задание", "21-12-24")
task_manager.add_task_and_date("Пойти в спортзал", "12-09-2024")
task_manager.add_task_and_date("Прочитать статью", "01-12-2024")
task_manager.add_task_and_date("Написать письмо", "20-11-20024")

task_manager.display_not_completed_tasks()

task_manager.mark_task_completed("Пойти в спортзал")
task_manager.mark_task_completed("Написать письмо")

task_manager.display_not_completed_tasks()

task_manager.all_task_date("01-12-2024")
task_manager.all_task_date("02-12-2024")