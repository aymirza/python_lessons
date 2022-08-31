def say_hello():
    print("Hello")

say_hello()
print("Bye")
print("Программа завершена-_1_Otkiritie_i_zakritie_faylovv\n")


def say_hello2():
    print("Hello")

def say_goodbye():
    print("Good Bye")

say_hello2()
say_goodbye()
print("Программа завершена-2\n")

print("Локалные функции")
def print_messages():
    def say_hello3():
        print("Hello")
    def say_goodbye2():
        print("Good Bye")

    say_hello3()
    say_goodbye2()

print_messages()
print("Программа завершена-3\n")

print("Организация программы и функция main")
def main():
    say_hello()
    say_goodbye()
main()




