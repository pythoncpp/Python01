# 1. list of first 10 numbers
# 2. collect all even values

# the filter will work only if
# - the function return True / False


def function1():
    numbers = list(range(1, 11))
    for value in numbers:
        if value % 2 == 0:
            print(value)


# function1()


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def function2():
    numbers = list(range(1, 11))
    for value in numbers:
        # if is_even(value) == True:
        if is_even(value):
            print(value)


# function2()


def function3():
    numbers = list(range(1, 11))
    even_numbers = []
    for value in numbers:
        if is_even(value):
            even_numbers.append(value)

    print(numbers)
    print(even_numbers)


# function3()


def function4():
    numbers = list(range(1, 11))
    even_numbers = list(map(is_even, numbers))
    print(numbers)
    print(even_numbers)


# function4()


def function5():
    numbers = list(range(1, 11))
    even_numbers = list(filter(is_even, numbers))
    print(numbers)
    print(even_numbers)


# function5()


def function6():
    numbers = list(range(1, 11))
    is_odd = lambda x: (x % 2 != 0)
    odd_numbers = list(filter(is_odd, numbers))
    print(odd_numbers)


# function6()


def function7():
    numbers = list(range(1, 11))
    odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(numbers)
    print(odd_numbers)
    print(even_numbers)


function7()


def function8():
    cars = [
        {"model": "i20", "company": "hyundai", "price": 7.5},
        {"model": "i10", "company": "hyundai", "price": 5.5},
        {"model": "nano", "company": "tata", "price": 2.5},
        {"model": "fortuner", "company": "toyota", "price": 15},
    ]

    # (car price < 6)
    for car in cars:
        if car['price'] < 6:
            print(car['model'])


# function8()


def function9():
    cars = [
        {"model": "i20", "company": "hyundai", "price": 7.5},
        {"model": "i10", "company": "hyundai", "price": 5.5},
        {"model": "nano", "company": "tata", "price": 2.5},
        {"model": "fortuner", "company": "toyota", "price": 15},
    ]

    affordable_cars = list(filter(lambda car: car['price'] < 6, cars))
    print(affordable_cars)
    print(list(filter(lambda car: car['price'] > 6, cars)))


function9()








