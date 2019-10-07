def function1():
    print("inside function1")


# function1()

# function alias
# function2 = function1
# print("type of function2: ", type(function2))
#
# function2()


def function2(param):
    # param = function1
    print("param: ", param)
    print("type of param: ", type(param))

    # make a call to the function
    param()


# function2(10)
# function2("test")
# function2(True)

# num = 100
# function2(num)

# call function2 with function1 as a param
# function2(function1)

def function3():
    print("inside function3")


function2(function3)
function2(function1)
