import numpy as np


def function1():
    a1 = np.array([10, 20, 30, 40])
    print(a1)
    print(a1.ndim)
    print(a1.shape)

    a2 = a1.reshape([2, 2])
    print(a2)
    print(a2.ndim)
    print(a2.shape)
    print(a2[0][0])


# function1()


def function2():
    a1 = np.array([
        [10, 20, 30],
        [40, 50, 60]
    ])
    print(a1)
    print(a1.ndim)
    print(a1.shape)
    print(a1[0][0])
    print(a1[1][2])

    a2 = a1.reshape([3, 2])
    print(a2)
    print(a2.ndim)
    print(a2.shape)

    a3 = a1.reshape([1, 6])
    print(a3)
    print(a3.ndim)
    print(a3.shape)

    a4 = a1.reshape([6, 1])
    print(a4)
    print(a4.ndim)
    print(a4.shape)

    print(a1)
    print(a1.ndim)
    print(a1.shape)

    print(a1[0][0])


# function2()


