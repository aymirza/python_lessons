message = "Hello world"
print(message)

name = "Tom"
print(name)

text = ("Laudate omnes gentes laudate "
        "Magnificat in secula")
print(text)

'''
Это комментарий
'''
text = ''' Laudate omnes get 
Magnificat in sacula
Et anima mea laudate
Magnificat in secula
'''
print(text)

print("\n")

# Управление последовательности в строки

text = "Message: \n\"Hello World\""
print(text)

path = "C:\python\name.txt"
print(path)
path = r"C:\python\name.txt"
print(path)

# Вставка значений в строку

userName = "Tom"
userAge = 37
user = f"name: {userName} age: {userAge}"
print(user)

# Обращение к символам строки
string = "Hello world"
c0 = string[0]
print(c0)
c6 = string[6]
print(c6)

string = "Hello World"
c1 = string[-1]
print(c1)
c5 = string[-5]
print(c5)

print("\n")

# Перебор строки
string = "Hello World"
for char in string:
    print(char)
print("\n")

# Получение подстроки
string = "Hello world"
sub_string = string[:5]
print(sub_string)
sub_string = string[2:5]
print(sub_string)

sub_string = string[2:9:2]
print(sub_string)


# Объдинение строк
name = "Tom"
surname = "Smith"
fullname = name+" "+surname
print(fullname)
print("\n")

name = "Tom"
age = 33
info = "Name : "+name+" Age: "+str(age)
print(info)

# Повторение строки
print("a "*5)
print("Hello "*4)
print("\n")

# Сравнение строк

str1 = "1a"
str2 = "aa"
str3 = "Aa"

print(str1 > str2)
print(str2 > str3)
print("\n")

str1 = "Tom"
str2 = "tom"

print(str1 == str2 )
print(str1.lower() == str2.lower())
print(str1.upper() == str2.upper())
print(str1.lower() == str2.upper())
print("\n")

# Функции ord и len

print(ord("A"))

string = "Hello world"
length = len(string)
print(length)

for char in string:
    print(ord(char))
print("\n")

# Поиск строке
string = "hello world"
exist = "hello" in string
print(exist)
exist = "sword" in string
print(exist)

