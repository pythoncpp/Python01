# closure
def executor(function):
    def inner_function(p1, p2):
        print('-*-' * 10)

        # print("p1 = ", p1)
        # print("p2 = ", p2)

        function(p1, p2)
        print('-*-' * 10)
        print()

    return inner_function


def add(p1, p2):
    print("addition = ", p1 + p2)


def subtract(p1, p2):
    print("subtraction = ", p1 - p2)


def multiply_1(p1, p2):
    print("multiplication = ", p1 * p2)


def divide_1(p1, p2):
    print("division = ", p1 / p2)


# add(10, 20)
# add(40, 50)
# add(60, 70)

executor_add = executor(add)
executor_add(10, 20)
executor_add(40, 50)
executor_add(60, 70)

executor_sub = executor(subtract)
executor_sub(10, 20)
executor_sub(60, 40)
executor_sub(60, 50)

# multiply = executor(multiply_1)
# multiply(10, 30)


