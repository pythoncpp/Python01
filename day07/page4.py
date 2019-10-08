# closure
def outer_function():
    print("inside outer function")

    def inner_function():
        print("inside inner function")

    return inner_function


# function alias
# my_return_value = inner_function
my_return_value = outer_function()
print("my_return_value = ", my_return_value)
print("type of my_return_value = ", type(my_return_value))
my_return_value()

# function alias
# my_outer_function = outer_function
# my_outer_function()


# def add(x, y):
#     return x + y
#
#
# result = add(10, 20)
# print("result = ", result)





