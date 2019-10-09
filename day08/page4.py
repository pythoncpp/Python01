def decorator(function):
    def wrapper(*args, **kwargs):
        print("-*-" * 20)
        function(*args, **kwargs)
        print("-*-" * 20)
    return wrapper


@decorator
def square(num):
    print("square =", (num ** 2))


square(20)


@decorator
def add(p1, p2):
    print("addition: ", (p1 + p2))


add(40, 50)



