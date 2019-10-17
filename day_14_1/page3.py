import numpy as np


def function1():
    # array with custom values
    a1 = np.array([10, 20, 30, 40, 50])
    print(a1)

    # array with range
    a2 = np.arange(1, 11)
    print(a2)

    # array with all zeros
    a3 = np.zeros(10)
    print(a3)

    a4 = np.zeros([2, 3], dtype=np.int8)
    print(a4)

    # array with all ones
    a5 = np.ones(10)
    print(a5)

    a6 = np.ones([4, 4], dtype=np.int8)
    print(a6)


# function1()


def function2():
    # a1 = np.arange(1, 11)
    a1 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

    # indexing
    print('a1[0]: ', a1[0])
    print('a1[-1]: ', a1[-1])

    # slicing
    print(a1[3:6])
    print(a1[3:])
    print(a1[:6])
    print(a1[:])


# function2()


def function3():
    l1 = [10, 20, 30]
    l2 = [40, 50, 60]
    print('l1 + l2 = ', (l1 + l2))

    def add():
        l3 = []
        for index in range(len(l1)):
            l3.append(l1[index] + l2[index])
        print(l3)

    add()

    print("l1 * 5 = ", (l1 * 5))


# function3()


def function4():
    a1 = np.array([10, 20, 30])
    a2 = np.array([40, 50, 60])

    # broadcasting operators
    print('a1 + a2 = ', (a1 + a2))
    print('a1 - a2 = ', (a1 - a2))
    print('a1 / a2 = ', (a1 / a2))
    print('a1 * a2 = ', (a1 * a2))

    print("a1 * 5 = ", (a1 * 5))
    print("a1 + 5 = ", (a1 + 5))
    print("a1 - 5 = ", (a1 - 5))
    print("a1 / 5 = ", (a1 / 5))


# function4()


def function5():
    a1 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

    print(a1)
    print(a1[4:8])

    # select the values at 2nd, 6th and 8th position
    print(a1[[2, 6, 8]])
    print(a1[[False, False, True, False, False, False, True, False, True, False]])

    # broadcasting operations
    print("a1 > 50 = ", (a1 > 50))
    print("a1 <= 80 = ", (a1 <= 80))

    # filtering
    print("values > 50 = ", (a1 > 50))
    print("values > 50 = ", a1[a1 > 50])
    print("values <= 80 = ", a1[a1 <= 80])


function5()