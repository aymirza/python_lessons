first_name = "Tom"
text = f"Hello, {first_name}"
print(text)

name = "Bob"
age = 23
info = f"Name: {name}\t Age: {age}"
print(info)
print("\n")

# Именованные параметры
text = f"Hello, {first_name}".format(first_name="Tom")
print(text)

info = "Name: {name}\t Age: {age}".format(name="Tom",age=23)
print(info)
print("\n")

# Параметры по позиции

info = "Name: {0}\t Age: {1}".format("Bob",23)
print(info)

text = "Hello, {0} {0} {0}".format("Tom")
print(text)
print("\n")

# Подстановки

welcome = "Hello {:s}"
name = "Tom"
formatted_welcome = welcome.format(name)
print(formatted_welcome)

source = "{:d} символов"
number = 5
target = source.format(number)
print(target)














