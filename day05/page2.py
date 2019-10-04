def function1():
    # empty tuple
    # numbers = ()
    numbers = tuple()
    print(numbers)
    print(type(numbers))


# function1()

def function2():
    # int
    numbers = (10)
    print(numbers)
    print(type(numbers))

    # numbers = 40

    # str
    countries = ("india")
    print(countries)
    print(type(countries))


# function2()


def function3():
    # tuple with one int value
    numbers = (10, )
    print(numbers)
    print(type(numbers))

    # tuple with one string value
    countries = ("india", )
    print(countries)
    print(type(countries))


# function3()


def function4():
    print("enter number1: ")
    num1 = int(input())

    print("enter number2: ")
    num2 = int(input())

    numbers = (num1, num2)
    print(numbers)


# function4()


def function5():
    numbers = []
    for index in range(2):
        print("enter value ", (index + 1))
        value = int(input())
        numbers.append(value)

    numbers_tuple = tuple(numbers)
    print(numbers_tuple)


# function5()


def function6():
    numbers = (10, 20, 30, 40, 50)

    # for value in numbers:
    #     print(value)

    for index in range(len(numbers)):
        print(numbers[index])


# function6()


def function7():
    # tuple
    numbers = (10, 4, 2, 6, 8, 1)

    # tuple => list
    numbers_list = list(numbers)
    numbers_list.sort()

    # list
    print(numbers_list)

    numbers_sorted = tuple(numbers_list)

    # tuple
    print(numbers_sorted)

    # delete the older tuple
    del numbers

    # print(numbers)


function7()
















