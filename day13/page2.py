def file_reader(file_name):
    file = open(file_name, 'r')
    data = file.read()
    print('data: ', data)
    file.close()

# try:
#     file_reader('my_file_2.txt')
# except:
#     print('file does not exist')


def function1():
    try:
        file_reader('my_file_3.txt')
    except:
        print('exception in function1')


# function1()


def function2():
    file_reader('my_file_3.txt')


try:
    function2()
except:
    print('exception handled at the time of calling function2')

