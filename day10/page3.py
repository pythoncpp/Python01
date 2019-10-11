class Person:

    # initializer
    def __init__(self, name, address, age):
        print('inside __init__')
        self.__name = name
        self.__address = address
        self.__age = age
        self.__file = open('test.file', 'w')
        self.__file.write('something in the file')

    # de-initializer
    def __del__(self):
        print('inside __del__')
        self.__file.close()

    # facilators
    def write_data(self, data):
        self.__file.write(data)

    def can_vote(self):
        if self.__age >= 18:
            print("yes")
        else:
            print("no")

    def print_details(self):
        print('name: ', self.__name)
        print('address: ', self.__address)
        print('age: ', self.__age)
        print()

    # setters / mutators
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if (age > 0) and (age < 100):
            self.__age = age
        else:
            print('invalid age value')

    def set_address(self, address):
        self.__address = address

    # getters / inspectors
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_address(self):
        return self.__address


# allocated the memory
person = Person('person 1', 'pune', 30)

# can not be used inside the program
# person.phone = '+9134544'

print('hello ', person.get_name())
person.can_vote()
person.print_details()
person.write_data('this is another data')


# NEVER CALL THE ___INIT__ AND __DEL__ METHODS EXPLICITLY
# person.__del__()

# deallocate the memory
del person


print("line 1")
print("line 2")
print("line 3")
print("line 4")
print("line 5")
print("line 6")
