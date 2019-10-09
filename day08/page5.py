# open(): used to open a file


def function1():
    # open the file into write mode
    file = open('my_file.txt', 'w')

    # write the data into the file
    file.write("India is my country.\n")

    # close the file
    file.close()


# function1()


def function2():
    file = open('my_file.txt', 'a')
    file.write("All indians are my brothers and sisters.\n")
    file.write("I love my country.")
    file.close()


# function2()


def function3():
    # open the file in read mode
    file = open('my_file.txt', 'r')

    # read the data from the file
    # data = file.read()

    # get only first 10 characters from the file
    # data = file.read(10)
    # print(data)

    # read the data line by line
    lines = file.readlines()
    # print(lines)
    
    for line in lines:
        print(line)

    # close the file
    file.close()


function3()

















