# Multilevel inheritance

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


class Manager(Employee):

    def __init__(self, name, employee_id, department):
        Employee.__init__(self, name, employee_id)
        self._department = department

    def print_manager_details(self):
        Employee.print_employee_details(self)
        print('department: ', self._department)


manager = Manager('manager 1', 2, 'account')
manager.print_manager_details()