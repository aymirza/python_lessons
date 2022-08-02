class Person1:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Name: {self.__name}")


class Employee1(Person1):
    def work(self):
        print(f"{self.name} works")

tom = Employee1("Tom")
print(tom.name)
tom.display_info()
tom.work()
print("Программа закончена\n")

# Класс работника
class Employee:
    def work(self):
        print("Employee works")
# класс студента
class Student:
    def study(self):
        print("Student studies")

class WorkingStudent(Employee,Student): # Наследование от классов Employee и Student
    pass

# класс работающего студента
tom = WorkingStudent()
tom.work()
tom.study()


