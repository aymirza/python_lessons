message = lambda: print("Hello")

message()
print("Программа завершена\n")

square = lambda n: n * n
print(square(4))
print(square(5))
print("Программа завершена\n")

sum = lambda a, b: a + b
print(sum(4, 5))
print(sum(5, 6))
print("Программа завершена\n")


def do_operation(a, b, operation):
    result = operation(a, b)
    print(f"result = {result}")


do_operation(5, 4, lambda a, b: a + b)
do_operation(5, 4, lambda a, b: a * b)
print("Программа завершена\n")

def select_operation(choice):
    if choice == 1:
        return lambda a,b:a+b
    elif choice == 2:
        return  lambda a,b:a-b
    else:return lambda a,b:a*b

operation = select_operation(1)
print(operation(10,6))

operation = select_operation(2)
print(operation(10,6))

operation = select_operation(3)
print(operation(10,6))
print("Программа завершена\n")






