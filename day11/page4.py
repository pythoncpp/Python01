class Person:

    def __init__(self):
        self.name = 'person1'
        self.address = 'pune'

    def print_person_details(self):
        print('name: ', self.name)
        print('address: ', self.address)


class Student(Person):

    # initialize the Student class object
    def __init__(self):
        # initialize the parent/base Person class
        Person.__init__(self)
        self.roll = 1

    def print_student_details(self):
        print('roll: ', self.roll)
        print('name: ', self.name)
        print('address: ', self.address)


person = Person()
print(person.__dict__)
person.print_person_details()

student = Student()
print(student.__dict__)
student.print_person_details()
student.print_student_details()
