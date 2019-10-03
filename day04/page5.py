# string: character
# - collection of characters


def function1():
    ch = 'a'
    print("ch = ", ch, "type = ", type(ch))

    str_1 = 'This is my car. My car is gray.'
    print(str_1.lower())
    print(str_1.upper())
    print(str_1.capitalize())
    print(str_1.swapcase())


# function1()


def function2():
    str_1 = 'This is my car. My car is gray.'

    print("car appears: ", str_1.count('car'))
    print("is appears: ", str_1.count('is'))
    print("a appears: ", str_1.count('a'))
    print("car appears on index: ", str_1.index('car', 16))


# function2()


def function3():
    str_1 = 'This is my car. My car is gray.'

    # convert string to list of characters
    list_of_characters = list(str_1)
    print(list_of_characters)
    print(type(list_of_characters))
    list_of_characters.reverse()
    print(list_of_characters)

    # convert the list of characters to the string
    str_2 = ''.join(list_of_characters)
    print(str_2)


# function3()


def function4():
    list_1 = ['1', '2', '3', '4', '5']

    print(''.join(list_1))
    print('-'.join(list_1))
    print('*'.join(list_1))

    countries = ['india', 'usa', 'uk']

    print(''.join(countries))
    print(','.join(countries))
    print(', '.join(countries))


# function4()

def function5():
    str_1 = 'This is my car. My car is gray.'
    print(str_1[0])
    print(str_1[-1])
    print(str_1[5:7])
    print(str_1[11:14])
    print(str_1[16:])
    print(str_1[:15])
    print(str_1[:])
    print(str_1[::-1])


# function5()


def function6():
    str_1 = 'This is my car. My car is gray.'

    sentences = str_1.split('.')
    print(sentences)

    words = str_1.split(' ')
    print(words)


# function6()


def function7():
    url = "http://mydomain.com?firstname=steve&lastname=jobs"
    # firstname = steve
    # lastname = jobs

    # split the url using ?
    parts = url.split('?')
    print(parts)

    domain_name = parts[0]
    query_string = parts[1]

    query_string_parameters = query_string.split('&')
    print(query_string_parameters)

    # iterate over the list of string
    for parameter in query_string_parameters:
        parts = parameter.split('=')
        # print(parts)
        print("key = ", parts[0], " and value = ", parts[1])


function7()
