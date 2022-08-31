print("Условная конструкция if")
language1 = "english"
if language1 == "english":
    print("Hello")
print("End-_1_Otkiritie_i_zakritie_faylovv if\n")


language2 = "russian"
if language2 == "english":
    print("Hello")
else:
    print("Привет")
print("End-2 if-else\n")


language3 = "russian"
if language3 == "english":
    print("Hello")
    print("World")
else:
    print("Привет")
    print("мир")
print("End-3 else\n")

language4 = "german"
if language4 == "english":
    print("Hello")
    print("World")
elif language4 == "german":
    print("Hallo")
    print("Welt")
else:
    print("Привет")
    print("мир")
print("End-4 elif\n")


print("\nВложенноые конструкции if")
language5 = "english"
daytime = "morning"
if language5 == "english":
    print("English")
    if daytime == "morning":
        print("Good morning")
    else:
        print("Goog evening")
print("End-5\n")

language6 = "russian"
daytime2 = "morning"
if language6 == "english":
    if daytime2 == "morning":
        print("Good morning")
    else:
        print("Good evening")
else:
    if daytime2 == "morning":
        print("Доброе утро")
    else:
        print("Добрый вечер")












