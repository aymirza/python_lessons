print("Цикл while-1")
number = 1
while number <= 5:
    print(f"number = {number}")
    number +=1
print("Работа программы завершена\n")

print("Цикл while-2")
number2 = 1
while number2 < 5:
    print(f"number = {number2}")
    number2 +=1
else:
    print(f"number2 = {number2}. Работа цикла завершена")
print("Работа программы завершена\n")


print("Цикл for-1")
message = "hello"
for c in message:
    print(c)
print("Работа программы завершена\n")

message2 = "Hello"
for c in message2:
    print(c)
else:
    print(f"Последний символ: '{c}'. Цикл завершен")
print("Работа программы завершена\n")

print("Вложенные циклы")
i = 1
j = 1
while i < 4 :
    while j <4:
        print(i*j,end="\t")
        j +=1
    print("\n")
    j=1
    i += 1

print("\nВыход из цикла. break и continue")

number3 = 0
while number3 < 5:
    number3 += 1
    if number3 == 3:
        break
    print(f"number = {number3}")




