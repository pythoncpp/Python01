def function1():
    numbers = list(range(1, 101))

    # get the twice of every number
    # print(list(map(lambda x: x * 2, numbers)))
    print([value * 2 for value in numbers])


# function1()


def function2():
    numbers = list(range(1, 101))

    # get even numbers
    # print(list(filter(lambda x: x % 2 == 0, numbers)))
    print([value for value in numbers if value % 2 == 0])


function2()
