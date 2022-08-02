def get_message():
    return "Hello METANIT.COM"


message = get_message()
print(message)
print(get_message())
print("Завершение программа\n")


def double(number):
    return 2 * number


result1 = double(4)
result2 = double(5)
print(f"result1 = {result1}")
print(f"result2 = {result2}")
print("Завершение программа\n")


def sum(a, b):
    return a + b


result = sum(4, 5)
print(f"sum(4,5) = {result}")
print(f"sum(3,5) = {sum(3, 5)}")
print("Завершение программа\n")


def print_person(name, age):
    if age > 120 or age < 1:
        print("Invalid age")
        return
    print(f"Name: {name} Age: {age}")
print_person("Tom",37)
print_person("Bob",-37)
