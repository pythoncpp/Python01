class Person:

    def __init__(self, name, address, age):
        self.__name = name
        self.__address = address
        self.__age = age

    def print_details(self):
        print('name: ', self.__name)
        print('address: ', self.__address)
        print('age: ', self.__age)


# person = Person('person1', 'pune', 30)
# person.print_details()


class Student:

    def __init__(self, name, address, age, roll, school):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__roll = roll
        self.__school = school

    def print_details(self):
        print('name: ', self.__name)
        print('address: ', self.__address)
        print('age: ', self.__age)
        print('roll: ', self.__roll)
        print('school: ', self.__school)
        print()


student_1 = Student('student 1', 'pune', 20, 1, 'school 1')
student_1.print_details()















