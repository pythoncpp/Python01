
def function1():
    numbers = [10, 20, 30, 40]

    # for value in numbers:
    #     print(value)

    for index in range(len(numbers)):
        print(numbers[index])


# function1()


def function2():
    # row: 2
    # col: 2
    numbers = [
        [10, 20],
        [30, 40]
    ]

    # print(numbers[0][0])
    # print(numbers[0][1])
    # print(numbers[1][0])
    # print(numbers[1][1])

    for collection in numbers:
        # print(type(collection))
        for value in collection:
            print(value)


# function2()


def function3():
    # rows x cols = 2x4
    numbers = [
        [10, 20, 30, 40],
        [50, 60, 70, 80]
    ]

    # print(numbers[1][2])

    print("rows: ", len(numbers))
    print("cols in row 0: ", len(numbers[0]))
    print("cols in row 1: ", len(numbers[1]))

    for row in range(len(numbers)):
        # print(row)
        # print(numbers[row])
        # print(len(numbers[row]))
        for col in range(len(numbers[row])):
            print("value: ", numbers[row][col])
        print()


# function3()


def function4():
    # list of lists
    numbers = [
        [10, 20],
        [30, 40, 50, 60],
        [70, 80, 90, 100, 110, 120, 130]
    ]

    # print("# rows = ", len(numbers))
    # print("# cols in row 0: ", len(numbers[0]))
    # print("# cols in row 1: ", len(numbers[1]))
    # print("# cols in row 2: ", len(numbers[2]))

    # for row in numbers:
    #     for col in row:
    #         print(col)
    #     print()

    for row in range(len(numbers)):
        # print(row)
        # print("cols in ", row , " = ", len(numbers[row]))
        for col in range(len(numbers[row])):
            print(numbers[row][col])
        print()


# function4()


def function5():
    numbers_1 = [10, 20, 30, 40]

    numbers_2 = [
        [10, 20],
        [30, 40]
    ]

    print(numbers_1)
    numbers_1.reverse()
    print(numbers_1)

    print(numbers_2)
    # numbers_2.reverse()
    # print(numbers_2)

    numbers_2[0].reverse()
    numbers_2[1].reverse()
    print(numbers_2)


function5()





















