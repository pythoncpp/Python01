# function alias
# - second name given to an older function


def function1():
    print("inside function1")


# function1()


def function2():
    num_1 = 100
    num_2 = num_1

    print("num_1 = ", num_1)
    num_1 = 500
    print("num_1 = ", num_1)

    print("num_2 = ", num_2)
    num_2 = 1000
    print("num_2 = ", num_2)


# function2()

def function3(p1, p2):
    print("inside function3")
    addition = p1 + p2
    return addition


# call the function and get the returned value
# result = function3(10, 20)
# print("result = ", result)


def function4():
    print("inside function4")


# function4()

num = 100
num_1 = num

# function alias
function5 = function4

function5()
function5()
function5()
function5()
function5()
















