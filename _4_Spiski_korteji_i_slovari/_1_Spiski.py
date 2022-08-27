numbers=[1,2,3,4,5]
people = ["Tom","Sam","Bob"]

print(numbers)
print(people)
print("Завершение программы\n")

numbers1 = [1,2,3,4,5]
numbers2 = list(numbers1)
print(numbers2)

letters = list("Hello")
print(letters)
print("Завершение программы\n")

numbers = [5]*6
print(numbers)

people = ["Tom"]*3
print(people)

students = ["Bob","Sam"]* 2
print(students)
print("Завершение программы\n")


# Обрашение к элементам списка

people = ["Tom","Bob", "Sam"]
print(people[0])
people[1]="Mike"
print(people)
print("Завершение программы\n")

# Перебор элементов

people = ["Tom","Sam","Bob"]
for person in people:
    print(person)
print("Завершение программы\n")

people = ["Tom","Sam","Bob"]
i=0
while i<len(people):
    print(people[i])
    i += 1
print("Завершение программы\n")

# Сравнение список
number1 = [1,2,3,4,5]
number2 = list([1,2,3,4,5])
if number1 == number2:
    print("number1 equal to number2")
else:
    print("number1 is not equal to number2")

# Добавление и удаление элементов
people = ["Tom","Bob"]
# добавляем в конец списка
people.append("Alice")
print(people)
# добавляем на вторую позицию
people.insert(1, "Bill")
print(people)
# добавляем набор элементов
people.extend(["Mike","Sam"])
print(people)
# получаем индекс элемента
index_of_tom = people.index("Tom")
print(index_of_tom)
# удаляем по этому индексу
removed_item = people.pop(index_of_tom)
print(people)
#удаляем последний элемент
last_item = people.pop()
print(people)
# удаляем элемент "Alice"
people.remove("Alice")
print(people)
# удаляем все элементы
people.clear()
print(people)
print("Завершение программы\n")

# Проверка наличие элемента
people = ["Tom","Bob","Alice","Sam"]
if "Alice" in people:
    people.remove("Alice")
    print(people)
print("Завершение программы\n")

# удаление с помощью del
people = ["Tom","Bob","Alice","Sam","Bill","Kate","Mike"]
print(people)
del people[1]
print(people)
del people[:3]
print(people)
print("Завершение программы\n")

# Подсчет вхождений
people = ["Tom","Bob","Alice","Tom","Bil","Tom"]
people_count = people.count("Tom")
print(people_count)
print("Завершение программы\n")

# Сортировка
people = ["Tom","Bob","Alice","Sam","Bill"]
people.sort()
print(people)
people.reverse()
print(people)

people = ["Tom","bob","Alice","sam","Bill"]
people.sort(key=str.lower)
print(people)
print("Завершение программы\n")

# Максимальное и минимальное значения
numbers = [9,21,24,31,54,4,1,5]
print(min(numbers))
print(max(numbers))
print("Завершение программы\n")

# Капирование списков
people1 = ["Tom","Bob","Alice"]
people2 = people1
people2.append("Sam")
print(people1)
print(people2)

people2 = people1.copy()
people2.append("Mike")
print(people1)
print(people2)
print("Завершение программы\n")

# Соединение списков
people3 = people1+people2
print(people3)
print("Завершение программы\n")

people4 = [
    ["Tom", 37],
    ["Sam",21],
    ["Bob",10]
]
print(people4[0])
print(people4[0][0])

person = list()
person.append("Bill")
person.append(41)
people4.append(person)
print(people4[-1])
print(people4)
people4[-1].append("+79895649465")
people4[-1].pop()
print(people4[-1])
print(people4)
people4.pop(-1)
print(people4)
people4[0]=["Sam",18]
print(people4)

for person in people4:
    for item in person:
        print(item, end=" | ")







