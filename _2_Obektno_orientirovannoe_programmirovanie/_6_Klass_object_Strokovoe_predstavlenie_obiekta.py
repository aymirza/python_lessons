class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name:{self.name} Age: {self.age}")

tom = Person("Tom", 23)
print(tom)
print("Программа закончена\n")

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_info(self):
        print(self)

    def __str__(self):
        return f"Name: {self.name} Age: {self.age}"

tom = Person("Tom",23)
print(tom)
tom.display_info()