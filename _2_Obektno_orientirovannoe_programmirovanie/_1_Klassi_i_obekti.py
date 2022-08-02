# Методы классов
class Person:
    def say_hello(self):
        print("Hello")
tom = Person()
tom.say_hello()
print("Программа закончена\n")

class Person:
    def say(self,message):
        print(message)

tom = Person()
tom.say("Hello METANIT.COM")
print("Программа закончена\n")

class Person:
    def say(self,message):
        print(message)

    def say_hello(self):
        self.say("Hello work")

tom = Person()
tom.say_hello()
print("Программа закончена\n")

# Конструкторы

class Person:
    def __init__(self):
        print("Создание объекта Person")
    def say_hello(self):
        print("Hello")

tom = Person()
tom.say_hello()
print("Программа закончена\n")

# Атрибуты объекта
class Person:
    def __init__(self, name):
        self.name = name
        self.age = 1
tom = Person("Tom")

# обращение к атрибутам
# получение значений
print(tom.name)
print(tom.age)
# изменение значения
tom.age = 37
print(tom.age)
tom.company = "Microsoft"
print(tom.company)
print("Программа закончена\n")


class Person:
    def __init__(self,name):
        self.name = name
        self.age = 1

    def display_info(self):
        print(f"Name: {self.name} Age: {self.age}")

tom = Person("Tom")
tom.age = 37
tom.display_info()

bob = Person("Bob")
bob.age = 41
bob.display_info()





