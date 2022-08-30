import csv

FILENAME = "users_2.csv"

users = [
    {"name": "Tom", "age": 28},
    {"name": "Alice", "age": 31},
    {"name": "Bob", "age": 34}
]

with open(FILENAME, "w", newline="") as file:
    columns = ["name", "age"]
    writer = csv.DictWriter(file, fieldnames=["name","age"])
    writer.writeheader()

    # запись несколько строк
    writer.writerows(users)

    user = {"name": "Sam", "age":25}
    # запись одной строки
    writer.writerow(user)

with open(FILENAME, "r", newline="") as file:
    reader = csv.DictWriter(file)
    for row in reader:
        print(row["name"],"-",row["age"])
