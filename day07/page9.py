def logger(function):
    def inner_function(p1, p2):
        print("p1: ", p1, ", p2: ", p2)
        result = function(p1, p2)
        print("returned value: ", result)
        print()

    return inner_function


@logger
def divide(p1, p2):
    result = 0
    if p2 == 0:
        print("not possible")
    else:
        result = p1 / p2
        print("division = ", result)
    return result


# divide(100, 40)
divide(100, 0)
