class Person:

    def print_details(self):
        print("name: ", self.name)
        print("address: ", self.address)
        print("age: ", self.age)
        print()

    def can_vote(self):
        if self.age >= 18:
            print("yes... :)")
        else:
            print("no... :(")

    def transfer(self, address):
        # the person is relocating
        self.address = address


person_1 = Person()
person_1.name = "person 1"
person_1.address = "Pune"
person_1.age = 30
print(person_1.__dict__)

# can_vote(person_1)
# print_details(person_1)

# person_1.can_vote()
# person_1.print_details()

# transfer(person_1, 'mumbai')
# person_1.transfer('mumbai')
# person_1.print_details()

#
# person_2 = Person()
# person_2.name = "person 2"
# person_2.address = "mumbai"
# person_2.age = 10
# print(person_2.__dict__)
#
# person_2.can_vote()
# person_2.print_details()

# def my_function():
#     print("inside function")
#
#
# print(my_function.__code__)
# print(my_function.__code__.co_names)
# print(my_function.__code__.co_code)
#
#
# import dis
# print(dis.dis(my_function))
