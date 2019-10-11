class Person:

    # public: no underscore
    # private: double underscore
    # protected: single underscore

    def __init__(self, name, address):
        self._name = name
        self._address = address

    # property: to access the method as a attribute using dot syntax
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def name(self):
        return self._name

    # def set_name(self, name):
    #     self.__name = name
    #
    # def get_name(self):
    #     return self.__name
    #
    # def set_address(self, address):
    #     self.__address = address
    #
    # def get_address(self):
    #     return self.__address


# person = Person('person 1', 'pune')
# print(person.__dict__)
# print('name: ', person._name)
# print('name: ', person.name)
# print('address: ', person.address)
#
# person.address = 'mumbai'
#
# print('address: ', person.address)

# person.set_name('person1')
# person.set_address('pune')
#
# print('name: ', person.get_name())
# print('address: ', person.get_address())



class Car:

    def __init__(self, model, company, price, fuel_type):
        self._model = model
        self._company = company
        self._price = price

        # public
        self.fuel_type = fuel_type

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

    @property
    def company(self):
        return self._company

    # @company.setter
    # def company(self, company):
    #     if (company == 'tata') or (company == 'hyundai'):
    #         self._company = company
    #     else:
    #         print('invalid company')

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price


car = Car('nano', 'tata', 2.5, 'petrol')
print('model: ', car.model)
print('company: ', car.company)
print('price: ', car.price)

# car.set_model('nano 1.2')
car.model = 'nano 1.2'
car.price = 3.5
car.fuel_type = 'blah blah blah'

print('model: ', car.model)
print('company: ', car.company)
print('price: ', car.price)
print('fuel type: ', car.fuel_type)

















