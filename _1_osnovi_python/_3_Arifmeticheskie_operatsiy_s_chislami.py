print("Сложение двух чисел:   " + repr(6+2) )
print("Вычитание двух чисел: "+repr(6-2))
print("Умножение двух чисел: "+repr(6*2))
print("Деление двух чисел: "+repr(7/2))
print("Целочисленное деление двух чисел: "+repr(7//2))
print("Возведение в степень: "+repr(6**2))
print("Получение остатка от деления: "+repr(7%2))

'''
Операции     Направление

**           Справо налево

* / // %     Слева направо

+ -          Слева направо
'''
number =  3+4*5**2+7
print(number)

''' Арифметические операции с присвоением


+=   Присвоение результата сложения

-=   Присвоение результата вычитания

*=   Присвоение результата умножения

/=   Присвоение результата от деления

//=  Присвоение результата целочисленного деления

**=  Присвоение степени числа

%=   Присвоение остатка от деления

'''

number  = 10
number +=5
print("\n"+repr(number))

number-=3
print(number)

number*=4
print(number)

# Округдение функция round

first_number = 2.0001
second_number = 5
third_number = first_number/ second_number
print("\n"+repr(third_number))

first_number = 2.0001
second_number = 0.1
third_number = first_number+second_number
print("\nбез функция round: "+repr(third_number))
print("функция round: "+ repr(round(third_number)))
print("округление до двух знаков после запятой: "+repr(round(third_number, 2)))




