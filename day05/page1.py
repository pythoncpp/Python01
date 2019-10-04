def function1():
    # mutable: changed
    numbers_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers_2 = [[10, 20], [30, 40], [50, 60]]


# function1()


def function2():
    # immutable: can not be changed
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(type(numbers))


# function2()


def function3():
    countries = ("india", "usa", "uk", "japan")
    print(type(countries))


# function3()


def function4():
    # passing a list in tuple function
    numbers_1 = tuple([10, 20, 30, 40, 50])
    print(numbers_1)
    print(type(numbers_1))

    # passing a tuple in tuple function
    # please note the double parenthesis
    numbers_2 = tuple((10, 20, 30, 40, 50))
    print(numbers_2)
    print(type(numbers_2))


# function4()


def function5():
    numbers_1 = [10, 20, 30, 40, 50]
    print(numbers_1)

    # change the values in the list
    numbers_1[0] = 100
    numbers_1[1] = 200

    print(numbers_1)

    numbers_1.append(60)
    numbers_1.append(70)

    print(numbers_1)

    numbers_2 = (10, 20, 30, 40, 50)
    print(numbers_2)

    # CAN NOT change/update the values
    # numbers_2[0] = 100

    # CAN NOT append/remove element to and from the tuple
    # numbers_2.append(60)


function5()






