import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from datetime import datetime
from tkcalendar import Calendar, DateEntry

# Класс Task для представления задач
class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = False  # False означает, что задача не выполнена, True - выполнена

    def complete(self):
        self.status = True

    def __repr__(self):
        status = "Выполнена" if self.status else "Не выполнена"
        return f"Задача: {self.description}, Дедлайн: {self.deadline}, Статус: {status}"

# Класс TaskManagerApp для управления задачами и интерфейсом
class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        self.tasks = []

        # Виджеты интерфейса
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.label = tk.Label(self.frame, text="Описание задачи:")
        self.label.grid(row=0, column=0)

        self.task_description_entry = tk.Entry(self.frame, width=40)
        self.task_description_entry.grid(row=0, column=1, padx=10)

        self.label_deadline = tk.Label(self.frame, text="Дедлайн:")
        self.label_deadline.grid(row=1, column=0)

        self.deadline_entry = DateEntry(self.frame, width=37, background='blue', foreground='white',
                                        borderwidth=2, date_pattern='yyyy-mm-dd')
        self.deadline_entry.grid(row=1, column=1, padx=10)

        self.add_task_button = tk.Button(self.frame, text="Добавить задачу", command=self.add_task)
        self.add_task_button.grid(row=2, column=1, pady=10)

        self.tasks_listbox = tk.Listbox(self.root, width=80)
        self.tasks_listbox.pack(pady=10)

        self.complete_task_button = tk.Button(self.root, text="Отметить выполненным", command=self.complete_task)
        self.complete_task_button.pack(pady=5)

        self.update_tasks_listbox()

    def add_task(self):
        description = self.task_description_entry.get()
        deadline = self.deadline_entry.get()
        if description and deadline:
            task = Task(description, deadline)
            self.tasks.append(task)
            self.update_tasks_listbox()
            self.task_description_entry.delete(0, tk.END)
            self.deadline_entry.set_date(datetime.now())
        else:
            messagebox.showerror("Ошибка", "Описание задачи и дедлайн не могут быть пустыми.")

    def complete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.tasks[task_index].complete()
            self.update_tasks_listbox()
        else:
            messagebox.showwarning("Внимание", "Выберите задачу для отметки выполненной.")

    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, repr(task))

# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
