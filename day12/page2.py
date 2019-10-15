# Method Overriding
# - calling the method from type of object
# - to override a method
#   - keep the method name same as that of the base class method name

class Person:

    def __init__(self, name, address, age):
        self._name = name
        self._address = address
        self._age = age

    def print_details(self):
        # print('name: ', self._name)
        # print('address: ', self._address)
        print('called from Person class')

    def can_vote(self):
        return self._age >= 18


class Student(Person):

    def __init__(self, name, address, age, roll):
        super().__init__(name, address, age)
        self._roll = roll

    def print_details(self):
        # print('roll: ', self._roll)
        # super().print_details()
        print('called from Student class')


# person = Person('person 1', 'address 1', 30)
# person.print_details()
# print('person can vote: ', person.can_vote())

student = Student('student 1', 'address 1', 20, 1)
student.print_details()
print('student can vote: ', student.can_vote())
# student.my_method()
