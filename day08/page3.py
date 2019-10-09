def add_1(p1, p2):
    result = p1 + p2
    print("addition: ", result)


# add_1(10, 20)


def add_2(p1, p2, p3):
    result = p1 + p2 + p3
    print("addition: ", result)


# add_2(10, 20, 30)


def add_3(p1, p2, p3, p4):
    result = p1 + p2 + p3 + p4
    print("addition: ", result)


# add_3(10, 20, 30, 40)


# variable length argument function
# - function which can accept any number of parameters
def add(*args):
    print(*args)
    print(args)
    print(type(args))
    # sum = 0
    # for arg in args:
    #     # sum = sum + arg
    #     sum += arg
    # print("sum = ", sum)


# add(10)
# add(10, 20)
# add(10, 20, 30)
# add(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
# add(10, "20", True)
# add(10, 20, [30, 40, 50])


def function_va(*args, **kwargs):
    print(args)
    print(type(args))

    print(kwargs)
    print(type(kwargs))


# (10, 20): tuple
# function_va(10, 20)

# {p1: 10, p2: 20}: dict
# function_va(p1=10, p2=20)

# (10, 20): tuple, {p1: 30, p2: 40}: dict
# function_va(10, 20, p1=30, p2=40)
