def function1(p1, p2):
    return p1 / p2


# try to execute this block
try:
    result = function1(10, 0)
# used to except the exception
# will be executed only in case of exception is raised
except ZeroDivisionError:
    print("except block")
    print('error: second param can not be zero')
# will be executed only in case of no exception is raised
else:
    print("else block")
    print('result: ', result)
# will be executed in case of no exception or at lease one exception
finally:
    print("finally block")
    print('this is finally block')
