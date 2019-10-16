def function1(p1, p2):
    division = p1 / p2
    print('division: ', division)


def function2(file_name):
    file = open(file_name, 'r')
    print('data: ', file.read())
    file.close()


try:
    function1(10, 0)
    function2('my_file_2.txt')

# used to handle FileNotFoundError
except FileNotFoundError:
    print('FileNotFoundError')

# used to handle ZeroDivisionError
except ZeroDivisionError:
    print('ZeroDivisionError')

# generic except block
# can be used to handle any type exception
except:
    print('exception occurred')
