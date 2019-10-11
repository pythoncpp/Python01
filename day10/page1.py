# class definition
class Person:

    # default initializer
    def __init__(self):
        print('inside __init__')


# print(Person.__dict__)
# print(Person.__dir__)
# print(dir(Person))


# class instanciation
# person = Person()
# person = Person()


class Car:

    # custom
    def __init__(self, model, company, price):
        print('inside __init__')
        self.model = model
        self.company = company
        self.price = price

    def print_details(self):
        print('model: ', self.model)
        print('company: ', self.company)
        print('price: ', self.price)


car = Car('i20', 'hyundai', 7.5)
car.print_details()
