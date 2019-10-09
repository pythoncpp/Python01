def my_closure():
    def inner_function():
        print("inside inner function")

    return inner_function


# function = my_closure()
# function()


def my_decorator(function):
    def wrapper_function():
        print("inside a wrapper function")
        function()

    return wrapper_function


@my_decorator
def my_function():
    print("inside my_function")


# my_function()

# my_function_alias = my_function
# my_function_alias()

# with decoration
# decorator = my_decorator(my_function)
# decorator()

my_function()
