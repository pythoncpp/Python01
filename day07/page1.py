def function1():
    numbers = list(range(1, 11))

    print(numbers)

    # squares
    print(tuple(map(lambda x: x ** 2, numbers)))

    # cubes
    print(list(map(lambda x: x ** 3, numbers)))

    # even numbers
    print(tuple(filter(lambda x: x % 2 == 0, numbers)))

    # odd numbers
    print(list(filter(lambda x: x % 2 != 0, numbers)))

    # square of even numbers
    print(tuple(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))))

    # cube of odd numbers
    print(list(map(lambda x: x ** 3, filter(lambda x: x % 2 != 0, numbers))))


function1()
