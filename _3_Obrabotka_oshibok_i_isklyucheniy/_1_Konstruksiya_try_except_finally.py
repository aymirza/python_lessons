string = "5"
numbers = int(string)
print(numbers)
print(type(numbers))
print(string)
print(type(string))
print("Завершение программы\n")
# ошибка
# string2 = "Hello"
# number = int(string2)
# print(number)

# try...except
try:
    number2 = int(input("Введите число: "))
    print("Введите число: ", number2)
except:
    print("Преобразование прошло неудачно")
print("Завершение программы\n")

# Блок finally
try:
    number3 = int(input("Введите число: "))
    print("Введенное число: ", number3)
except:
    print("Преобразование прошло неудачно")
finally:
    print("Блок try завершил выполнение")
print("Завершение программы\n")


