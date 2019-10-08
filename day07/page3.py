# global: function1
def function1():
    print("inside function1")
    num = 100
    print("num = ", num)


# function1()
# print("type of function1: ", type(function1))


# global: function2
def function2():
    print("inside function2")
    num2 = 200
    print("num2 = ", num2)

    # function1()


# function2()


# global function
def function3():
    print("inside function3")
    # local
    num3 = 300

    # local: my_function
    # inner function
    # nested function
    def my_function():
        print("inside my_function")

    print("type of num3: ", type(num3))
    print("type of my_function: ", type(my_function))

    my_function()


# function3()

# local variable
# print("num3 = ", num3)

# inner function
# my_function()


def function4():
    num4 = 400

    print("inside function4")
    print("num4 = ", num4)

    num4 = 800
    print("num4 = ", num4)

    def inner_function():
        print("inside inner_function")

        # inner function can by default access all the members
        # of outer function

        # used to update the local member of outer function
        nonlocal num4
        print("num4 = ", num4)
        num4 = 900
        print("num4 = ", num4)

        num5 = 500
        print("num5 = ", num5)

    inner_function()

    # outer function can not access any inner function's member
    # print("inside function4, num5 = ", num5)

function4()






















