class Company:

    def __init__(self, name, employees):
        self._name = name
        self._employees = employees
        self._index = 0

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self._employees):
            employee = self._employees[self._index]
            self._index += 1
            return employee
        else:
            raise StopIteration()

    def print_employees(self):
        for employee in self._employees:
            print(employee)


# company_1 = Company('company 1', ('emp1', 'emp2', 'emp3', 'emp4', 'emp5'))
# company_1.print_employees()

# for employee in company_1:
#     print(employee)

# iterator = iter(company_1)
# try:
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
# except StopIteration:
#     # print('end of list')
#     pass


class MyNumber:

    def __init__(self, number, count=10):
        self._number = number
        self._count = count
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < self._count:
            value = (self._index + 1) * self._number
            self._index += 1
            return value
        else:
            raise StopIteration()


my_number = MyNumber(2, 20)
for number in my_number:
    print(number)


table_3 = MyNumber(3)
for number in table_3:
    print(number)

# for index in range(1, 11):
#     print(2 * index)


