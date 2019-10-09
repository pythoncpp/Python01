def decorator_1(function):
    def wrapper(*args, **kwargs):
        print("inside decorator_1")
        function(*args, **kwargs)

    return wrapper


def decorator_2(function):
    def wrapper(*args, **kwargs):
        print("inside decorator_2")
        function(*args, **kwargs)

    return wrapper


def decorator_3(function):
    def wrapper(*args, **kwargs):
        print("inside decorator_3")
        function(*args, **kwargs)

    return wrapper


# decorator chaining
@decorator_1
@decorator_2
@decorator_3
def function1():
    print("inside function1")



# d_3 = decorator_3(function1)
# d_3()
#
# d_2 = decorator_2(d_3)
# d_2()
#
# d_1 = decorator_3(d_2)
# d_1()

function1()




















