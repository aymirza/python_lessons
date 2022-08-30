try:
    somefile = open("hello.txt", "w")
    try:
        somefile.write("Hello world AAA")
        print("Данные записано ")
    except Exception as e:
        print(e)
    finally:
        somefile.close()
except Exception as ex:
    print(ex)
print("Завершение программы\n")

with open("hello.txt", "w") as somefile:
    somefile.write("Hello Aymirza")
