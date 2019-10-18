import numpy as np


def function1():
    a1 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

    # print(a1.ndim)
    # print(a1.dtype)
    # print(a1.shape)
    # print(a1.itemsize)
    # print(a1.size)
    # print(a1.data)

    # indexing
    # print(a1[0])
    # print(a1[-1])
    # print(a1[[2, 4, 6, 7, 8]])
    # print(a1[[False, False, True, False, True, False, True, True, True, False]])

    # slicing
    # print(a1[2:6])
    # print(a1[:6])
    # print(a1[2:])
    # print(a1[:])

    # broadcast operator
    # print(a1 + 5)
    # print(a1 - 5)
    # print(a1 > 50)

    # filtering
    print(a1[a1 > 50])


# function1()


def function2():
    a1 = np.array([10, 20, 30])
    print(a1.shape)
    print(a1.ndim)

    print(a1)
    print()

    # a2 = a1.reshape([2, 2])
    a2 = a1.reshape([1, 3])
    print(a2.shape)
    print(a2.ndim)
    print(a2)
    print()

    a3 = a1.reshape([3, 1])
    print(a3.shape)
    print(a3.ndim)
    print(a3)


function2()