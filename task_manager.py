class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = False  # False означает, что задача не выполнена, True - выполнена

    def complete(self):
        self.status = True

    def __repr__(self):
        status = "Выполнена" if self.status else "Не выполнена"
        color = "\033[92m" if self.status else "\033[91m"  # Зеленый для выполненных, красный для невыполненных
        reset_color = "\033[0m"
        return f"{color}Задача: {self.description}, Дедлайн: {self.deadline}, Статус: {status}{reset_color}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        new_task = Task(description, deadline)
        self.tasks.append(new_task)
        print(f"Добавлена задача: {new_task}")

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].complete()
            print(f"Задача выполнена: {self.tasks[task_index]}")
        else:
            print("Неверный индекс задачи")

    def wip_task(self):
        print("Все задачи:")
        for task in self.tasks:
            print(task)

# Пример использования
manager = TaskManager()
manager.add_task("Купить продукты", "2024-06-15")
manager.add_task("Закончить проект", "2024-06-20")
manager.add_task("Позвонить другу", "2024-06-12")

manager.complete_task(0)  # Отметить первую задачу как выполненную

manager.wip_task()  # Вывести список всех задач
