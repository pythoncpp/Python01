import numpy as np
import sys


def function1():
    print("---  python collection  ---")
    l1 = [10, 20, 30, 40, 50, "test", True]
    print(l1)
    print('type of l1: ', type(l1))
    print('count of l1: ', len(l1))
    print('type of l1[0]: ', type(l1[0]))
    print('type of l1[5]: ', type(l1[5]))
    print('type of l1[6]: ', type(l1[6]))

    print()
    print("---  numpy  ---")

    # immutable collection of similar items
    a1 = np.array([10, 20, 30, 40, 50, "test", True])
    print(a1)
    print('type of a1: ', type(a1))
    print('count of a1: ', a1.size)
    print('type of a1[0]: ', type(a1[0]))
    print('type of a1[5]: ', type(a1[5]))
    print('type of a1[6]: ', type(a1[6]))


# function1()


def function2():
    print("---  python collection  ---")
    l1 = [10, 20, 30, 40, 50]
    print('type l1: ', type(l1))
    print("size of one item inside l1: ", sys.getsizeof(l1[0]))
    print('total size of l1: ', len(l1) * sys.getsizeof(l1[0]))

    print()
    print("---  numpy  ---")

    a1 = np.array([10, 20, 30, 40, 50])
    print('type a1: ', a1.dtype)
    print("size of one item inside a1: ", a1.itemsize)
    print('total size of a1: ', a1.size * a1.itemsize)

    a2 = np.array([10, 20, 30, 40, 50], dtype=np.int64)
    print("size of one item inside a2: ", a2.itemsize)

    a3 = np.array([10, 20, 30, 40, 50], dtype=np.int32)
    print("size of one item inside a3: ", a3.itemsize)

    a4 = np.array([10, 20, 30, 40, 50], dtype=np.int16)
    print("size of one item inside a4: ", a4.itemsize)

    a5 = np.array([10, 20, 30, 40, 50], dtype=np.int8)
    print("size of one item inside a5: ", a5.itemsize)


# function2()


def function3():
    a1 = np.array([10, 20, 30, 40, 50])
    print(a1)
    print('type: ', a1.dtype)
    print('itemsize: ', a1.itemsize)
    print('dimensions: ', a1.ndim)
    print('shape: ', a1.shape)


function3()


def function4():
    a1 = np.array([
        [10, 20, 30],
        [40, 50, 60]
    ])
    print(a1)
    print('type: ', a1.dtype)
    print('itemsize: ', a1.itemsize)
    print('dimensions: ', a1.ndim)
    print('shape: ', a1.shape)


# function4()