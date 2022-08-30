with open("hello2.txt", "w") as file:
    file.write("Hello 2 File \ngoodBye world")
print("Завершение программы\n")

with open("hello3.txt", "w") as hello_file:
    print("Hello, world",file=hello_file)
print("Завершение программы\n")

with open("hello2.txt", "r") as file:
    for line in file:
        print(line,end="")
print("Завершение программы\n")

with open("hello2.txt.","r") as file:
    str1 = file.readline()
    print(str1)
    str2 = file.readline()
    print(str2)
print("Завершение программы\n")

with open("hello2.txt", "r") as file:
    line = file.readline()
    while line:
        print(line, end="")
        line = file.readline()
print("\nЗавершение программы\n")

with open("hello2.txt", "r") as file:
    content = file.read()
    print(content)
print("Завершение программы\n")







