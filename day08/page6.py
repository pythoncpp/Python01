def logger(function):
    def wrapper(*args, **kwargs):
        # write the parameters to the file
        file = open('my_app.log', 'a')

        file.write('-' * 80)
        file.write("\n")
        file.write("Function Name: ")
        file.write(function.__name__)
        file.write("\n")
        file.write("Input Parameters: \n")
        file.write(str(args))
        file.write("\n")
        file.write(str(kwargs))
        file.write("\n")

        returned_value = function(*args, **kwargs)
        file.write("Return value: ")
        file.write(str(returned_value))
        file.write("\n")
        file.write('-' * 80)
        file.write('\n')

        file.close()

    return wrapper


@logger
def add(p1, p2):
    result = p1 + p2
    print("addition: ", result)
    return result


# add(10, 30)
# add(40, 50)


@logger
def divide(p1, p2):
    result = p1 / p2
    print("division: ", result)
    return result

@logger
def square(num):
    result = num ** 2
    print("square =", result)
    return result


# square(4)

divide(10, 0)


# print("function name: ", square.__name__)
# print("function name: ", add.__name__)

