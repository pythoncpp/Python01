class Car:

    def print_details(self):
        print('model: ', self.model)
        print('company: ', getattr(self, 'company'))
        print('price: ', getattr(self, 'price'))
        print()

    def can_afford(self):
        if self.price <= 6:
            print('Yes. I can afford it.')
        else:
            print('Nope. I can not afford it.')


car_1 = Car()
car_1.model = 'i20'
car_1.company = 'hyundai'
car_1.price = 7.5

car_1.can_afford()
car_1.print_details()


car_2 = Car()
car_2.model = 'fabia'
car_2.company = 'Skoda'
car_2.price = 5.5

car_2.can_afford()
car_2.print_details()


car_3 = Car()
car_3.model = 'innova'
car_3.company = 'toyota'
car_3.price = 20

car_3.can_afford()
car_3.print_details()
