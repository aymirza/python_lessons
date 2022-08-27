class Person:
    type = "Person"
    description = "Describes a person"

print(Person.type)
print(Person.description)

Person.type = "Class Person"
print(Person.type)
print("Программа зевершено\n")

# Сатические методы
class Person:
    __type = "Person"

    @staticmethod
    def print_type():
        print(Person.__type)
Person.print_type()

tom = Person()
tom.print_type()



