def add(p1, p2):
    print("addition: ", (p1 + p2))


def subtract(p1, p2):
    print("subtraction: ", (p1 - p2))


def multiply(p1, p2):
    print("multiplication: ", (p1 * p2))


def divide(p1, p2):
    print("division: ", (p1 / p2))


def executor(function):
    function(10, 20)
    function(30, 40)
    function(50, 60)
    function(70, 80)


# executor(add)
# executor(subtract)
# executor(multiply)
# executor(divide)

def executor_1(function, p1=0, p2=0):
    function(p1, p2)


# executor_1(add, 10, 20)
# executor_1(add, 20, 40)
# executor_1(add)


def executor_2(function1, function2, function3, function4):
    function1(30, 40)
    function2(30, 40)
    function3(30, 40)
    function4(30, 40)


executor_2(add, subtract, multiply, divide)



# # 10, 20
# add(10, 20)
# subtract(10, 20)
# multiply(10, 20)
# divide(10, 20)
#
# # 30, 40
# add(10, 20)
# subtract(10, 20)
# multiply(10, 20)
# divide(10, 20)
#
# # 50, 60
# add(10, 20)
# subtract(10, 20)
# multiply(10, 20)
# divide(10, 20)

