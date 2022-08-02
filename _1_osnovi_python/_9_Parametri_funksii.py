def say_hello(name):
    print(f"Hello, {name}")

say_hello("Tom")
say_hello("Aymirza")
print("Программа завершена-1\n")

def print_person(name,age):
    print(f"Name: {name}")
    print(f"Age: {age}")
print_person("Tom",37)
print("Программа завершена-2\n")

def say_hello2(name = "Tom"):
    print(f"Hello, {name}")

say_hello2()
say_hello2("Bob")
print("Программа завершена-3\n")

def print_person(name, age = 18):
    print(f"Name: {name} Age: {age}")
print_person("Bob")
print_person("Tom",37)
print("Программа завершена-4\n")

print("Неопределенное количество параметров")
def sum(*numbers):
    result = 0
    for n in numbers:
        result += n
    print(f"sum = {result}")
sum(1,2,3,4,5)
sum(3,4,5,6)


