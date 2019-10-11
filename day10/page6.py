# has-a
# composition


class Address:

    def __init__(self, city, state, pin):
        self.__city = city
        self.__state = state
        self.__pin = pin

    def print_details(self):
        print('city: ', self.__city)
        print('state: ', self.__state)
        print('pin code: ', self.__pin)


class Person:

    def __init__(self, name, age, city, state, pin):
        self.__name = name
        self.__age = age
        self.__address = Address(city, state, pin)

    def __del__(self):
        del self.__address

    def print_details(self):
        print('name: ', self.__name)
        print('age: ', self.__age)
        self.__address.print_details()


person1 = Person('person1', 30, 'pune', 'MH', 455233)
person1.print_details()
# person1.print_details()
# person1.print_details()

del person1

class House:
    pass
