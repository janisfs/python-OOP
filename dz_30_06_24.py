class Task():
    def __init__(self):
        self.tasks = []

    def add_task(self, deadline, description):
        self.tasks.append({'deadline':deadline, 'description':description, 'status': "Не выполнена"})

    def complete_tasks(self, description):
        for task in self.tasks:
            if task['description'] == description:
                task['status'] = "Выполнено"
                print(f"Задача {description} выполнена")
            else:
                print(f"Задача {description} не найдена")

    def show_tasks(self):
        print("Текущие задачи: ")
        for task in self.tasks:
            if task['status'] == "Не выполнена":
                print(f"{task['description']} - {task['deadline']}")

t = Task()
t.add_task("Прочитать книгу", "2024-06-01")
t.add_task("Пробежать марафон", "2024-06-05")
t.add_task("Починить машину", "2024-06-27")

t.show_tasks()

t.complete_tasks("Прочитать книгу")
