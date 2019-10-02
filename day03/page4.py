# get numbers from user and get the squares of them


def function1():
    # empty list
    # numbers = []
    numbers = list()
    print(numbers)

    # append (to the end of the list) a new value into the list
    numbers.append(10)
    print(numbers)

    numbers.append(20)
    print(numbers)

    numbers.append(30)
    print(numbers)


# function1()


def function2():
    numbers = []

    print("enter value: ")
    value = int(input())
    numbers.append(value)

    print("enter value: ")
    value = int(input())
    numbers.append(value)

    print("enter value: ")
    value = int(input())
    numbers.append(value)

    print(numbers)


# function2()

def function3():
    numbers = [1, 2, 3, 4, 5]
    for value in numbers:
        square = value * value
        print("square = ", square)


# function3()


def function4():
    numbers = [1, 2, 3, 4, 5]
    for value in numbers:
        # cube = value * value * value
        cube = value ** 3
        print("cube = ", cube)


# function4()


def function5():
    # [1, 2... 10]

    # upper bound of range is excluded from the list
    numbers_1 = list(range(1, 11))
    print(numbers_1)

    numbers_2 = list(range(1, 11, 2))
    print(numbers_2)

    numbers_3 = list(range(1, 11, 3))
    print(numbers_3)

    numbers_4 = list(range(1, 11, -1))
    print(numbers_4)

    numbers_5 = list(range(11, 1, -1))
    print(numbers_5)


# function5()


def function6():
    numbers = []

    # index_values = list(range(0, 3))
    # for index in index_values:

    print("number of values you want to enter: ")
    upper_bound = int(input())

    for index in range(upper_bound):
        print("enter value: ")
        value = int(input())
        numbers.append(value)

    print(numbers)


function6()


def function7():
    # range object (variable)
    r = range(1, 10)
    print(r)

    # convert the range object to list
    l = list(r)
    print(l)


# function7()
