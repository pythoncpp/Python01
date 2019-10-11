class Person:

    def __init__(self, name, address, age):
        # public members
        self.name = name
        self.address = address
        self.age = age

    def print_details(self):
        print('name: ', self.name)
        print('address: ', self.address)
        print('age: ', self.age)
        print()


person1 = Person('person1', 'pune', 30)
print(person1.__dict__)
# person1.print_details()
# person1.address = 10034234
# person1.age = 1000000
# person1.print_details()


class Car:

    def __init__(self, model, company):
        # private
        self.__model = model
        self.__company = company

    def print_details(self):
        print('model: ', self.__model)
        print('company: ', self.__company)


car = Car('nano', 'Tata')
print(car.__dict__)
# print('model: ', car._Car__model)
# car._Car__model = 'changed'
# print('model: ', car._Car__model)

# print('model: ', car.__model)
# car.print_details()
# car.__model = 1234
# car.__company = 56767
# print(car.__dict__)
# car.print_details()



