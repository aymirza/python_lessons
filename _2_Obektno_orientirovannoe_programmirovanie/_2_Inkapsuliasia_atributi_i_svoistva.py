class Person:
    def __init__(self, name):
        self.name = name
        self.age = 1

    def display_info(self):
        print(f"Имя: {self.name} \tВозраст: {self.age}")

tom = Person("Tom")
tom.name = "Человек-паук"
tom.age = -129
tom.display_info()
print("Программа закончена\n")


# Инкапсулация
class Person:
    def __init__(self,name):
        self.__name = name
        self.__age = 1
    def set_age(self, age):
        if 1<age<110:
            self.__age=age
        else:
            print("Недоступный возраст")
    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def display_info(self):
        print(f"Имя: {self.__name} \tВозраст: {self.__age}")

tom = Person("Tom")
tom.display_info()
tom.set_age(-3486)
tom.set_age(48)
tom.display_info()
print("Программа закончена\n")

# Аннотация свойств
class Person:
    def __init__(self,name):
        self.__name = name
        self.__age = 1

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 1<age<110:
            self.__age = age
        else:
            print("Недопустимый возраст")

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Имя:{self.__name} \tВозраст:{self.__age}")

tom = Person("Tom")

tom.display_info()
tom.age = -3486
print(tom.age)
tom.age = 36
tom.display_info()










