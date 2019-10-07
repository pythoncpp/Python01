
def function1():
    numbers = list(range(1, 11))

    # square of only even numbers

    # get all even numbers
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

    # get squares
    squares = list(map(lambda x: x ** 2, even_numbers))

    print(squares)


# function1()


def function2():
    numbers = list(range(1, 11))

    # cube of only odd numbers
    cubes = list(map(lambda x: x ** 3, filter(lambda x: x % 2 != 0, numbers)))
    print(cubes)


# function2()


def function3():
    cars = [
        {"model": "i20", "company": "hyundai", "price": 7.5},
        {"model": "i10", "company": "hyundai", "price": 5.5},
        {"model": "nano", "company": "tata", "price": 2.5},
        {"model": "fortuner", "company": "toyota", "price": 15},
    ]

    # models of affordable cars
    affordable_cars = list(filter(lambda car: car['price'] < 6, cars))
    print(affordable_cars)

    models = tuple(map(lambda car: car['model'], affordable_cars))

    print(models)


# function3()


def function4():
    cars = [
        {"model": "i20", "company": "hyundai", "price": 7.5},
        {"model": "i10", "company": "hyundai", "price": 5.5},
        {"model": "nano", "company": "tata", "price": 2.5},
        {"model": "fortuner", "company": "toyota", "price": 15},
    ]

    companies = list(map(lambda car: car['company'], filter(lambda car: car['price'] > 6, cars)))
    print(companies)


function4()
