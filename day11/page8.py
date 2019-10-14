# Single inheritance

class Person:

    def __init__(self, name):
        self._name = name

    def print_person_details(self):
        print('name: ', self._name)


class Employee(Person):

    def __init__(self, name, employee_id):
        Person.__init__(self, name)
        self._employee_id = employee_id

    def print_employee_details(self):
        Person.print_person_details(self)
        print('employee id: ', self._employee_id)


employee = Employee('empoyee 1', 1)
employee.print_employee_details()
