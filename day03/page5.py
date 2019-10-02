def function1():
    numbers = [10, 3, 4, 5, 6, 2, 3, 5]
    print(numbers)

    # reverse the order of the list members
    numbers.reverse()

    print(numbers)


# function1()


def function2():
    numbers = [10, 3, 4, 5, 6, 2, 3, 5]
    print(numbers)

    # sort all the numbers in ascending order
    numbers.sort()

    print(numbers)


# function2()


def function3():
    numbers = [10, 3, 4, 5, 6, 2, 3, 5]
    print(numbers)

    # sort all the numbers in ascending order
    numbers.sort(reverse=False)
    print(numbers)

    # sort all the numbers in descending order
    numbers.sort(reverse=True)
    print(numbers)


# function3()

def function4():
    numbers = [1, 2, 3, 4, 5]
    print(numbers)

    # remove the last value from the list
    value = numbers.pop()

    print("popped value = ", value)

    print(numbers)


# function4()


def function5():
    numbers = [1, 2, 3, 4, 5]
    print(numbers)

    # add 10 at index 1
    numbers.insert(1, 10)

    print(numbers)

    # add 10 at index 1
    numbers.insert(4, 20)

    print(numbers)


# function5()

def function6():
    numbers = [10, 20, 30, 40, 50]
    print(numbers)

    # remove a value from the list
    numbers.remove(30)

    print(numbers)


# function6()


def function7():
    numbers = [10, 20, 30, 40, 50]
    print(numbers)

    # remove a value at index 1
    numbers.pop(1)

    print(numbers)


# function7()


def function8():
    numbers = [10, 20, 30, 40, 50, 60]
    print(numbers)

    # getting the value at position 0
    print(numbers[0])

    # setting/updating  the value at position 0
    numbers[0] = 11
    numbers[1] = 21
    numbers[2] = 31
    numbers[3] = 41
    numbers[4] = 51

    print(numbers)

    print("count of values in the numbers: ", len(numbers))


# function8()


def function9():
    numbers = [10, 20, 30, 40, 50]

    # for value in numbers:
    #     print(value)

    # print(numbers[0])
    # print(numbers[1])
    # print(numbers[2])
    # print(numbers[3])
    # print(numbers[4])

    for index in range(len(numbers)):
        print("value = ", numbers[index])


# function9()


def function10():
    numbers = [10, 20, 30, 40, 50, 10, 40, 30, 10, 20]

    print("10 appears ", numbers.count(10))
    print("20 appears ", numbers.count(20))
    print("100 appears ", numbers.count(100))

    print("enter value you want to search: ")
    value = int(input())
    print(value, " appears ", numbers.count(value),  " times")


# function10()


def function11():
    numbers = [10, 20, 30, 40, 50, 10, 40, 30, 10, 20]

    # first occurance of 10
    print("index of 10: ", numbers.index(10))

    # occurance after 1st index of 10
    print("index of 10: ", numbers.index(10, 1))

    # occurance after 1st index of 10
    # print("index of 10: ", numbers.index(10, 1, 4))

    print("index of 50: ", numbers.index(50))


# function11()


def function12():
    numbers_1 = [10, 20, 30, 40]
    numbers_2 = [50, 60, 70, 80]
    print(numbers_1)
    print(numbers_2)

    numbers_1.extend(numbers_2)

    print(numbers_1)
    print(numbers_2)


# function12()

def function13():
    numbers_1 = [10, 20, 30, 40, 50, 60]
    numbers_2 = [1, 2, 3, 4, 5, 0]

    # [9, 18, 27, 36, 45]

    result = []
    for index in range(len(numbers_1)):
        value_1 = numbers_1[index]
        value_2 = numbers_2[index]
        result.append(value_1 - value_2)

    print(result)


function13()

















