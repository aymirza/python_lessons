try:
    number = int(input("Введите число: "))
    print("Введенное число: ", number)
except ValueError:
    print("Преобразование прошло неудачно")
print("Завершение программы\n")

try:
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))
    print("Результат деления: ", number1/number2)
except ValueError as e:
    print("Преобразование прошло неудачно", e)
except ZeroDivisionError as e:
    print("Попытка деления числа на ноль ", e)
except BaseException:
    print("Общее исключение")
print("Завершение программы")
