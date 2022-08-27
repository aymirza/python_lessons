tom = ("Tom",23)
print(tom)
tom2 = "Tom",24
print(tom2)

data = ["Tom",37, "Google"]
tom3 = tuple(data)
print(tom3)
print(len(tom3))
print("Завершение программы\n")

tom = ("Tom",37,"Google","software developer")
print(tom[0])
print(tom[2])
print(tom[1])
print(tom[3])

name,age,company,position = ("Tom",37,"Google","software developer")
print(name)
print(age)
print(company)
print(position)
print("Завершение программы\n")

# Получение подкортежей
tom = ("Tom",37,"Google","software developer")
# получаем подкортеж с 1 по 3 элемента(не включая)
print(tom[1:3])
print(tom[:3])
print(tom[1:])
print("Завершение программы\n")

# Перебор кортежей
tom = ("Tom",22, "Google")
for item in tom:
    print(item)

i = 0;
while i<len(tom):
    print(tom[i])
    i +=1

# Проверка наличия значения
user = ("Tom",22, "Google")
name = "Tom"
if name in user:
    print("Пользователя зовут Tom")
else:
    print("Ползаватель имеет другое имя")
