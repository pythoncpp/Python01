def executor(function):
    def inner_function(p1, p2):
        print("-*-" * 10)
        function(p1, p2)
        print("-*-" * 10)
        print()

    return inner_function


# executor_add = executor(add)
# executor_add(10, 20)

# @executor
def add(p1, p2):
    print("addition = ", p1 + p2)


# executor_sub = executor(subtract)
# executor_sub(10, 20)

# decorator
@executor
def subtract(p1, p2):
    print("subtraction = ", p1 - p2)


executor_add = executor(add)
executor_add(10, 20)
executor_add(40, 50)

# add(10, 20)
# add(40, 50)

# executor_sub = executor(subtract)
# executor_sub(50, 20)
subtract(50, 20)

# executor_sub = executor(subtract)
# executor_sub(100, 20)
subtract(100, 40)
