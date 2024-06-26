class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is now studying.")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super.__init__(name, age)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is now teaching {self.subject}")




anton = Student("Anton", 21, 1234)
anton.introduce()
anton.study()
anton.age +=2
anton.introduce()
