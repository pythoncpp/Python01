# slicing
# - retrieve only part of collection
# - syntax
#   <collection>[<lower>:<upper>:<stride>]
#   <collection>[<start>:<stop>:<stride>]
#   - the slicing will never include the upper bound
#   - stride: step count in range
# - the collection will NEVER get modified
#
# rules
#   - lower bound < upper bound
#   - the index values must be similar (both positive or both negative)
#   - upper bound is excluded from the slice


def function1():
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # for index in range(4):
    #     print(numbers[index])

    print(numbers[0:4])
    print(numbers[4:9])

    # excluding the last value
    print(numbers[-5:0])
    print(numbers[5:10])


# function1()


def function2():
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # get all the values
    print(numbers[0:10])

    # get all the values from even positions
    print(numbers[0:10:2])

    # get all the values from odd positions
    print(numbers[1:10:2])


    # index_values = list(range(1, len(numbers), 2))
    # print(index_values)
    #
    # for index in index_values:
    #     print(numbers[index])


# function2()


def function3():
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    print(numbers[0])

    # upper bound default value = last index of the collection
    print(numbers[0:])
    print(numbers[5:])

    print(numbers[5])
    print(numbers[:5])

    # value at 6th index
    print(numbers[6])

    # values at [6, 7, 8, 9]
    print(numbers[6:])

    # values at [0, 1, 2, 3, 4, 5]
    print(numbers[:6])


# function3()


def function4():
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # lower = 0, upper = 9, stride = 1
    print(numbers[:])
    print(numbers[::])

    # lower = 0, upper = 9, stride = 2
    print(numbers[::2])

    # lower = 0, upper = 9, stride = 2
    print(numbers[1::2])

    # reversing the collection
    print(numbers[::-1])

    print(numbers[4::-1])
    print(numbers[4:-1])


function4()

