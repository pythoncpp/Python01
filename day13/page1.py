def divide_without_exception_handling(p1, p2):
    division = p1 / p2
    return division

# print('10 / 5 = ', divide(10, 5))
# print('10 / 5 = ', divide(10, 0))


def divide(p1, p2):
    try:
        division = p1 / p2
        print('division: ', division)
    except:
        print('the second parameter is zero')


# divide(10, 5)
# divide(10, 0)

def file_reader(file_name):
    try:
        file = open(file_name, 'r')
        data = file.read()
        print('data: ', data)
        file.close()
    except:
        print('file does not exist')


# file_reader('my_file.txt')
file_reader('my_file_2.txt')
