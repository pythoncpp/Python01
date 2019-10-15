class Person:

    def __init__(self, name, address, age):
        self._name = name
        self._address = address
        self._age = age

    def print_details(self):
        print('name: ', self._name)
        print('address: ', self._address)
        print('age: ', self._age)

    # # used to convert the object into string representation
    def __str__(self):
        # return "from person class"
        # return "Person [name: {}, address: {}, age: {}]".format(self._name, self._address, self._age)
        return "Person [name: " + self._name + ", address: " + self._address + ", age: " + str(self._age) + "]"


person = Person('person1', 'pune', 30)
# person.print_details()
print(person)
print(person.__str__())

num = 10
print(num)
print(num.__str__())
