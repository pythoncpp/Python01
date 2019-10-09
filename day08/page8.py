# list comprehension

numbers = list(range(1, 11))


def function1():
    # print(numbers)
    # print(list(map(lambda x: x, numbers)))

    # selecting the value from the list
    # for value in numbers:
        # using the value
        # print(value)

    print([val for val in numbers])


# function1()


def function2():
    # numbers_1 = []
    # for value in numbers:
    #     numbers_1.append(value + 5)
    # print(numbers_1)

    # print(list(map(lambda x: x + 5, numbers)))
    print([value + 5 for value in numbers])


# function2()


def function3():
    # print(list(map(lambda x: x ** 2, numbers)))
    print([value ** 2 for value in numbers])
    print([value ** 3 for value in numbers])


# function3()


def function4():
    # even_numbers = []
    # for value in numbers:
    #     if value % 2 == 0:
    #         even_numbers.append(value)
    #
    # print(even_numbers)

    # print(list(filter(lambda x: x % 2 == 0, numbers)))
    print([value for value in numbers if value % 2 == 0])
    print([value for value in numbers if value % 2 != 0])


# function4()


def function5():
    # print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))))
    print([value ** 2 for value in numbers if value % 2 == 0])
    print([n ** 3 for n in numbers if n % 2 != 0])


# function5()


def function6():
    # countries = ["india", "usa", "uk", "japan"]
    # print([country for country in countries])

    cars = [
        {"model": "i20", "company": "hyundai", "price": 7.5},
        {"model": "i10", "company": "hyundai", "price": 5.5},
        {"model": "nano", "company": "tata", "price": 2.5},
        {"model": "fortuner", "company": "toyota", "price": 15},
    ]

    # print([car for car in cars])
    # print([car['model'] for car in cars])
    # print([car['model'] for car in cars if car['price'] < 6])
    print([car['company'] for car in cars if car['price'] > 6])


function6()





