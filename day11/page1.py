class Address:

    def __init__(self, city, state):
        self.__city = city
        self.__state = state

    def print_address(self):
        print("City: ", self.__city)
        print("State: ", self.__state)
        print()


class Person:

    def __init__(self, name, age, city, state):
        self.__name = name
        self.__age = age
        self.__address = Address(city, state)

    def print_details(self):

        # print person details
        print("name: ", self.__name)
        print("age: ", self.__age)

        # print address
        self.__address.print_address()


class House:

    def __init__(self, rooms, city, state):
        self.__rooms = rooms
        self.__address = Address(city, state)

    def print_details(self):
        print('rooms: ', self.__rooms)
        self.__address.print_address()


person = Person('person1', 20, 'pune', 'MH')
person.print_details()

house = House(3, 'mumbai', 'MH')
house.print_details()











