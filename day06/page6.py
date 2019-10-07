# 1. list of first 10 numbers
# 2. collect square of every number in the list


def function1():
    numbers = list(range(1, 11))
    for value in numbers:
        print("square = ", value ** 2)


# function1()


def function2():
    numbers = list(range(1, 11))
    squares = []
    for value in numbers:
        squares.append(value ** 2)

    print(numbers)
    print(squares)


# function2()


def square(num):
    print("num = ", num)
    return num ** 2


def function3():
    numbers = list(range(1, 11))
    squares = []
    for value in numbers:
        squares.append(square(value))

    print(numbers)
    print(squares)


# function3()


def function4():
    numbers = list(range(1, 11))
    squares = list(map(square, numbers))
    print(squares)


# function4()


def function5():
    numbers = list(range(1, 11))
    cubes = []
    for value in numbers:
        cubes.append(value ** 3)

    print(cubes)


# function5()


def function6():
    numbers = list(range(1, 11))
    cube = lambda x: x ** 3
    cubes = list(map(cube, numbers))
    print(cubes)


# function6()


def function7():
    numbers = list(range(1, 11))
    print(list(map(lambda x: x ** 3, numbers)))


# function7()


def function8():
    temperatures = [90, 98, 99, 97, 92, 95]
    temperatures_celcius = []
    for temperature in temperatures:
        celcius = (temperature - 32) * (5/9)
        temperatures_celcius.append(celcius)

    print(temperatures)
    print(temperatures_celcius)


# function8()


def function9():
    temperatures = [90, 98, 99, 97, 92, 95]
    print(list(map(lambda t: (t - 32) * (5/9), temperatures)))


# function9()


def function10():
    cars = [
        {"model": "i20", "company": "hyundai"},
        {"model": "i10", "company": "hyundai"},
        {"model": "nano", "company": "tata"},
        {"model": "fortuner", "company": "toyota"},
    ]

    for car in cars:
        print(car["model"])


# function10()


def function11():
    cars = [
        {"model": "i20", "company": "hyundai"},
        {"model": "i10", "company": "hyundai"},
        {"model": "nano", "company": "tata"},
        {"model": "fortuner", "company": "toyota"},
    ]

    # models = list(map(lambda car: car['model'], cars))
    # models.sort()
    # print(models)

    companies = list(map(lambda car: car['company'], cars))
    print(companies)


# function11()







