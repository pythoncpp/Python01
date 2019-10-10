class Person:

    # custom initializer
    def __init__(self, name, address, age, phone=''):
        self.name = name
        self.address = address
        self.age = age
        self.phone = phone

    def print_details(self):
        print('name: ', self.name)
        print('address: ', self.address)
        print('age: ', self.age)
        print('phone: ', self.phone)


person_1 = Person('person 1', 'pune', 30)
person_1.print_details()

person_2 = Person('person 2', 'mumbai', 10, '+912344434')
person_2.print_details()


