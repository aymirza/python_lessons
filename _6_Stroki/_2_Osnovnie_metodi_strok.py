string = "helloworld"
string2 = "Hello world 2"
print(string.isalpha())
print(string.islower())
print("\n")

string = input("Введите число: ")
if string.isnumeric():
    number = int(string)
    print(number)
else:
    print("Неправилное символ\n")

file_name = "hello.py"
start_with_hello = file_name.startswith("hello")
print(start_with_hello)
ends_with_exe = file_name.endswith("exe")
print(ends_with_exe)
print("\n")

string = "     Hello  world   "
string = string.strip()
print(string)
print("\n")

print("Iphone 7:","52000".rjust(10))
print("Huawei P10:", "36000".rjust(8))
print("\n")

welcome = "hello world! Goodbye world!"
index = welcome.find("wor")
print(index)

# поиск с 10-го индекса
index = welcome.find("wor",10)
print(index)

# поиск с 10 по 15 индекс
index = welcome.find("wor",10,15 )
print(index)
print("\n")

# Замена в строке
phone = "+1-234-567-89-10"

# замена дефисов на пробел
edited_phone = phone.replace("-"," ")
print(edited_phone)

# удаление дефисов
edited_phone = phone.replace("-","")
print(edited_phone)

# замена только первого дефиса
edited_phone = phone.replace("-","",1)
print(edited_phone)
print("\n")

# Разделение на подстроки
text = "Это был огромный, в два обхвата дуб, с обломанными ветвями и с обломанной корой"
# разделение по пробелам
splitted_text = text.split()
print(splitted_text)
print(splitted_text[6])

# разбиение по запятым
splitted_text = text.split(",")
print(splitted_text)
print(splitted_text[1])

# разбиение по первым пяти пробелам
splitted_text = text.split(" ",5)
print(splitted_text)
print(splitted_text[5])
print("\n")

# Соединение строки
words = ["Let", "me", "speak", "from", "my", "heart", "in", "English"]

# разделитель - пробел
sentence = " ".join(words)
print(sentence)

# разделитель - вертикальная черта
sentence = " | ".join(words)
print(sentence)

word = "hello"
joined_word = "|".join(word)
print(joined_word)






