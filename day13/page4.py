def function1(file_name):

    is_file_open = False
    try:
        file = open(file_name, 'r')
        is_file_open = True
        data = file.read()
        print('data: ', data)
    except FileNotFoundError:
        print('file does not exist')
    except IOError:
        print('IO Error')
    finally:
        print('finally block')
        if is_file_open:
            file.close()


# no exception will be raised
function1('my_file.txt')

# exception will be raised
function1('my_file_2.txt')