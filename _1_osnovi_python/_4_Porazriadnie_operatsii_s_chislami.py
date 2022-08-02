'''
При этом Python позволяет сразу определять число в двоичной форме. Для этого число в двоичной форме указывается после префикса 0b:
'''
number = 5  # в двойчной форме 101
print(f"number = {number:0b}")

number = 0b101
print(f"number = {number:0b}")
print(f"number = {number}")

print("цифры на двойчном форме")
number = 2
print(f"number = {number:0b}")
number = 3
print(f"number = {number:0b}")
number = 4
print(f"number = {number:0b}")
number = 6
print(f"number = {number:0b}")
number = 7
print(f"number = {number:0b}")

print("\nЛогические операции")
print("логическое умножение - &")
x1 = 2
y1 = 5
z1 = x1 & y1
print(f"x1 = {x1} -> {x1:0b}")
print(f"y1 = {y1} -> {y1:0b}")
print(f"z1 = {z1}")

print("логическое сложение - |")
x1 = 2
y1 = 5
z1 = x1 | y1
print(f"z1 = {z1}")
print(f"z1 = {z1:0b}\n")

x1 = 4
y1 = 5
z1 = x1 | y1
print(f"z1 = {z1}")
print(f"z1 = {z1:0b}")

print("логическое исключающее ИЛИ - ^")

x1 = 9
y1 = 5
z1 = x1 ^ y1
print(f"z1 = {z1}")
print(f"z1 = {z1:0b}\n")

x = 45
key = 102
encrypt = x ^ key
print(f"Зашифрованное число: {encrypt}")
decrypt = encrypt ^ key
print(f"Расшифрованное число: {decrypt}")

print("\nОперация сдвига\n")

a = 16
b = 2
c = a << b
print(c)

d = a >> b
print(d)
