class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Приватное поле '__age'

    def introduce(self):
        print(f"Hello, my name is {self.name}, and I am {self.__age} years old.")

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age < 0:
            raise ValueError("Age cannot be negative.")
        else:
            self.__age = new_age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is now studying.")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is now teaching {self.subject}")


# Создаем объект класса Person
person1 = Person("Anton", 30)
person1.introduce()  # Вывод: Hello, my name is Anton and I am 30 years old.

# Создаем объект класса Student
student1 = Student("Boris", 20, "с-1234")
student1.introduce()  # Вывод: Hello, my name is Boris, and I am 20 years old.
student1.study()      # Вывод: Student Boris is now studying.

# Создаем объект класса Teacher
teacher1 = Teacher("Valentin", 40, "Mathematics")
teacher1.introduce()  # Вывод: Hello, my name is Valentin, and I am 40 years old.
teacher1.teach()      # Вывод: Teacher Valentin is teaching Mathematics.

current_age = person1.get_age()
print(f"Current age: {current_age}")

person1.set_age(35)
person1.introduce()

