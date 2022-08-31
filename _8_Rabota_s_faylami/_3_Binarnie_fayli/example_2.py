import pickle

FILENAME = "users_2.dat"

users = [
    ["Tom",28,True],
    ["Alice",45,False],
    ["Bob",37,True]
]

with open(FILENAME, "wb") as file:
    pickle.dump(users, file)

with open(FILENAME, "rb") as file:
    users_from_file = pickle.load(file)
    for user in users_from_file:
        print("Имя: ", user[0], "\tВозраст: ", user[1], "\tЖенат(замужем): ", user[2] )