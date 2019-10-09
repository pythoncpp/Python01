def my_decorator(function):
    def wrapper(p1, p2):
        print('-' * 20)
        result = function(p1, p2)
        print("p1:", p1, ", p2:", p2, ", result:", result)
        print('-' * 20)
    return wrapper


def my_decorator_1(function):
    def wrapper(p1):
        print('-' * 20)
        result = function(p1)
        print("p1:", p1, ",result:", result)
        print('-' * 20)
    return wrapper


@my_decorator
def multiply(p1, p2):
    result = p1 * p2
    print("multiplication:", result)
    return result


@my_decorator
def divide(p1, p2):
    result = p1 / p2
    print("division:", result)
    return result


@my_decorator_1
def square(num):
    result = num ** 2
    print("square =", result)
    return result


@my_decorator_1
def convert_f_c(temperature):
    celcius = (temperature - 32) * (5/9)
    print("temperature: ", celcius)
    return  celcius


# decorator = my_decorator(multiply)
# decorator(5, 6)

# multiply(5, 6)
# divide(10, 5)

# decorator = my_decorator(square)
# decorator(6)

# square(6)

convert_f_c(98)