try:
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))
    if number2 == 0:
        raise Exception("Второе число не должно быть равно 0")
    print("Результат деление двух чисел: ", number1/number2)
except ValueError:
    print("Введены некорректные данные")
except Exception as e:
    print(e)
print("Завершение программы\n")

# Создание своих типов исключений
class PersonAgeException(Exception):
    def __init__(self,age,minage,maxage):
        self.age = age
        self.minage = minage
        self.maxage = maxage

    def __str__(self):
        return f"Недопустимое значение: {self.age} Возраст должен быть в диапазоне от {self.minage} до {self.maxage}"

class Person:
    def __init__(self,name,age):
        self.__name = name
        minage,maxage = 1,110
        if minage<age<maxage:
            self.__age = age
        else:
            raise PersonAgeException(age,minage,maxage)

    def display_info(self):
            print(f"Имя: {self.__name} Возраст: {self.__age}")

try:
    tom = Person("Tom",37)
    tom.display_info()
    bob = Person("Bob",-27)
    bob.display_info()
except PersonAgeException as e:
    print(e)