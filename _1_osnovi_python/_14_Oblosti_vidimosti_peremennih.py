# Локальный контекст
name = "Tom"

def say_hi():
    print("Hello",name)

def say_bye():
    print("Good Bye", name)

say_hi()
say_bye()
print("Программа завершена\n")

# Локальный контекст
def say_hi():
    name = "Sam"
    surname = "Johnson"
    print("Hello", name, surname)
def say_bye():
    name = "Tom"
    print("Good bye", name)

say_hi()
say_bye()
print("Программа завершена\n")

# Скрытие переменных
name = "Tom"

def say_hi():
    name = "Bob"
    print("Hello", name)

def say_bye():
    print("Good Bye", name)

say_hi()
say_bye()
print("Программа завершена\n")

# nonlocal
def outer():
    n = 5
    def inner():
        n=10
        print(n)

    inner()
    print(n)

outer()
print("Программа завершена\n")








