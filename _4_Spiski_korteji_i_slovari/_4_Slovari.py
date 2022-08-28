user = {1: "Tom", 2: "Bob",3:"Bill"}
print(user[2])
print("Завершение программы\n")

user_list=[
    ["+1111","Tom"],
    ["+2222","Bob"],
    ["+3333","Alice"]
]
print(user_list)
user_dict = dict(user_list)
print(user_dict)
print("Завершение программы\n")


users= {
    "+1111":"Tom",
    "+2222":"Bob",
    "+3333":"Alice"
}
key = "+1111"
if key in users:
    user = users[key]
    print(user)
else:
    print("Элемент не найдено")
print("Завершение программы\n")

user1 = users.get("+1111")
print(user1)
user2 = users.get("+2222","Unknown user")
print(user2)

# Удаление
users = {
    "+1111":"Tom",
    "+2222":"Bob",
    "+3333":"Alice"
}
del users["+2222"]
print(users)

users2 = {
    "+1111":"Tom",
    "+2222":"Bob",
    "+3333":"Alice"
}
key = "+1111"
if key in users2:
    del users2[key]
    print(f"Элемент с ключом {key} удален")
    print(users2)
else:
    print("Элемент не найден")


users3 = {
    "+1111":"Tom",
    "+2222":"Bob",
    "+3333":"Alice"
}
key = "+1111"
users4 = users3.pop(key)
print(users4)
print(users3)

users3.clear()
print(users3)

# Капирование и объединение словарей
users = {"11": "Ali","22":"Vali","333":"Sali"}
users2 = users.copy()
print(users)

# Update

users5 = {"44":"ffff","55":"DDD"}
users.update(users5)
print(users)

# перебор словаря
users7 = {
    "12":"Tom",
    "13":"Salli",
    "14":"Valli"
}
for key in users7:
    print(f"Phone:{key} User:{users7[key]}")

for key,value in users7.items():
    print(f"Phone: {key} User: {value}")







