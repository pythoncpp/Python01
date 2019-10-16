# custom exception
class InvalidAgeException(Exception):
    pass


class InvalidSalaryException(Exception):
    pass


def function1():
    print("enter name:")
    name = input()

    print("enter age: ")
    age = int(input())

    if (age < 20) or (age > 60):
        raise InvalidAgeException()

    print("enter salary: ")
    salary = int(input())

    if salary > 60000:
        raise InvalidSalaryException()

    print("name: {}, age: {}, salary: {}".format(name, age, salary))


try:
    function1()
except InvalidAgeException:
    print("invalid age")
except InvalidSalaryException:
    print("invalid salary")
except:
    print("invalid input")

