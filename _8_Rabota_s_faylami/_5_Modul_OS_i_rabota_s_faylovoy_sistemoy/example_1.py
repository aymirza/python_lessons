import os

# os.mkdir("hello")
# os.rmdir("hello")
# путь относительно текущего скрипта

# абсолютный путь
# os.mkdir("c://somedir")
# os.mkdir("c://somedir/hello")

# os.rename("C://somedir/hello", "C://somedir/somefile")

# os.remove("C://somedir/hello.txt")


filename = input("Введите путь к файлу: ")
if os.path.exists(filename):
    print("Указанный файл существует")
else:
    print("Файл не сушествует")
