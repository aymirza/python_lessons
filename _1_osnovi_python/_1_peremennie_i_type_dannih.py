'''
ключевые слов

False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield

'''

# целые число  по умалчение исползует десятичной системе

age = 21
print("Возрост:",age)

count = 15
print("Количество:",count, type(count))

# двоичную система

a = 0b11
b = 0b1011
c = 0b100001
print(a)
print(type(b),b)
print(c)

# восмеричную система
a = 0o7
b = 0o11
c = 0o17
print("\n",a)
print(b)
print(c)

# шеснадцатеричную система
a = 0x0A
b = 0xFF
c = 0XA1
print("\n",a)
print(b)
print(c)

# дробные число ( float )
height = 1.68
pi = 3.14
weight = 68.
print("\n",height)
print(type(pi),pi)
print(weight)

# число с плавающей точкой можно определять в экспоненциально записи,
# Число float может иметь только 18 значимых символов
# Число после экспоненты указывает степень числа 10

x = 3.9e3
print("\n",x)
x = 3.9e-3
print(x)

# комплексные числа
''' Тип complex представляет комплексные числа в формате
 вещественная_часть+мнимая_частьj - после мнимой части указывается суффикс j'''

complexNumber = 1+2j
print("\n",complexNumber)

# Строки, Тип str представляет строки
message = "Hello World!"
print("\n",message)
name = 'Tom'
print(name)

text = ("Laudate omnes gentes laudate "
        "Magnificat in secula ")
print(text)


''' Это комментарий '''

text2 = ''' Laudate omnes gentes laudate
Manifucat in secula
Et anima mea laudate
magnificat in secula
'''
print("\n"+text2)


text3 = "Message \n\"Hello World\""
print(text3)

path = "\nC:\python\name.txt\n"
print(path)

path2 = r"C:\python\name.txt"
print(path2)

userName = "Tom"
userAge = "37"
user = f"\nname:{userName} age:{userAge}"
print(user)

userId = "abc"  # тип str
print(userId)
print(type(userId))

userId = 234  #тип int
print(userId)
print(type(userId))









