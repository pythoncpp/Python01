class Person:

    # initializer
    # - method to initialise the attributes of the object
    # - gets called automatically / implicitly
    # - get called for every object of this class

    # default initializer
    # - does not accept any (custom) parameter
    # - used to initialize the attributes to their default values
    def __init__(self):
        print('inside __init__')
        self.name = ''
        self.address = ''
        self.age = 0

    def print_details(self):
        print('name: ', self.name)
        print('address: ', self.address)
        print('age: ', self.age)


person_1 = Person()
print(person_1.__dict__)
person_1.print_details()

# person_2 = Person()
# print(person_2.__dict__)
# person_2.print_details()
#
# person_3 = Person()
# print(person_3.__dict__)
# person_3.print_details()
#
# person_4 = Person()
# print(person_4.__dict__)
# person_4.print_details()
#
