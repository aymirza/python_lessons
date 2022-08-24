class Person:
    def __init__(self,name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Name: {self.__name}")

class Employee(Person):
    def __init__(self,name,company):
        super().__init__(name)
        self.company = company

    def display_info(self):
        super().display_info()
        print(f"{self.name} works")

tom = Employee("Tom","Microsoft")
tom.display_info()
print("Программа зевершена\n")


class Person1:
    def __init__(self, name,age):
        self.__name=name
        self.__age=age

    @property
    def get_name(self):
        return self.__name
    @property
    def get_age(self):
        return self.__age

    def display_info(self):
        print(f"Name:{self.__name} \tAge: {self.__age}")

class Employee1(Person1):
    def __init__(self,name,age,company,salary):
        super().__init__(name,age)
        self.company = company
        self.salary=salary

    def display_info(self):
        super().display_info()
        print(f"Company: {self.company} \tSalary:{self.salary}")

    def work(self):
        print(f"{self.salary} work")

tom1 = Employee1("Tom",37,"Apple","$1000")
tom1.display_info()
tom1.work()
print("Программа зевершена\n")

# Проверка типа объекта "isinstance()"
class Person2:
    def __init__(self,name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def do_nothing(self):
        print(f"{self.name} does nothing")

# класс работника
class Employee2(Person2):
    def work(self):
        print(f"{self.name} works")
# класс студента
class Student(Person2):
    def study(self):
        print(f"{self.name} studies")

def act(person):
    if isinstance(person,Student):
        person.study()
    elif isinstance(person, Employee2):
        person.work()
    elif isinstance(person, Person2):
        person.do_nothing()

tom2 = Employee2("Tom")
bob = Student("Bob")
sam = Person2("Sam")

act(bob)
act(tom2)
act(sam)


