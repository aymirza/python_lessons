FILENAME = "messages.txt"
messages = list()

for i in range(5):
    message = input("Введите строку "+ str(i+1)+": ")
    messages.append(message+"\n")

with open(FILENAME, "a") as file:
    for message in messages:
        file.write(message)


print("Считанное сообщения")
with open(FILENAME, "r") as file:
    for message in file:
        print(message, end="")
