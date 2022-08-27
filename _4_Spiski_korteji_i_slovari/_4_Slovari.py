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
