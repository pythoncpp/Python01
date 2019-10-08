def add(p1, p2):
    print("addition = ", p1 + p2)


def subtract(p1, p2):
    print("subtraction = ", p1 - p2)


def multiply(p1, p2):
    print("multiplication = ", p1 * p2)


def divide(p1, p2):
    print("division = ", p1 / p2)


# print("-------------")
# add(10, 20)
# print("-------------")
#
# print("-------------")
# subtract(10, 20)
# print("-------------")


def executor(function):
    print('-*-' * 10)
    function(10, 20)
    print('-*-' * 10)
    print()


executor(add)
executor(subtract)
executor(multiply)
executor(divide)

# multiply(10, 20)
# divide(10, 20)
