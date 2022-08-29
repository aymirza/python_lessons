users = {"Tom","Bob","Alice","Tom"}
print(users)
print("Завершение программы\n")

people = ["Mike","Bill", "Ted"]
users = set(people)
print(users)
print(len(users))
print("Завершение программы\n")

users = set(people)
users.add("Sam")
print(users)
print("Завершение программы\n")

user = "Bill"
if user in users:
    users.remove(user)
print(users)
print("Завершение программы\n")

users.clear()

# Перебор множеста
users = {"Tom","Bob","Alice"}
for user in users:
    print(user)
print("Завершение программы\n")

# Операция с множествами
student = users.copy()
print(student)

# union()
users2 = {"Sam", "Kate","Bob"}
users3 = users.union(users2)
print(users3)

# intersection()
users4 = users.intersection(users2)
print(users4)

# symmetric_difference()
user5 = users.symmetric_difference(users2)
print(user5)
print("Завершение программы\n")

# Отношения между множествами
# issubset()
users = {"Tom", "Bob", "Alice"}
superusers = {"Sam","Tom","Bob","Alice","Greg"}

print(users.issubset(superusers))
print(superusers.issubset(users))
print("Завершение программы\n")

# frozen set
users = frozenset({"Tom","Bob","Alice","Alone","Mike"})
print(users)
print(len(users))





