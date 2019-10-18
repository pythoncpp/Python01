import pandas as pd
import numpy as np


def function1():
    s1 = pd.Series([10, 20, 30, 40, 50, 60], dtype=np.int8)
    print(s1)
    print()

    s2 = pd.Series(["india", "usa", "uk", "japan"])
    print(s2)


# function1()


def function2():
    s1 = pd.Series([10, 20, 30, 40, 50, 60], dtype=np.int8)
    print(s1)

    # indexing
    print(s1[0])

    # converting the s1 to values array
    # it will print the last value in the array
    print(s1.values[-1])

    # s1 does not have any index value -1
    # this statement will raise an exception
    # print(s1[-1])


# function2()


def function3():
    s1 = pd.Series([10, 20, 30, 40, 50, 60], dtype=np.int8)
    print(s1)
    print()

    print(s1[0])
    print()

    # slicing
    print(s1[3:5])
    print()

    print(s1[3:])
    print()

    print(s1[:5])
    print()

    print(s1[:])
    print()


# function3()


def function4():
    s1 = pd.Series([10, 20, 30, 40, 50, 60], dtype=np.int8)
    print(s1)

    # broadcast operator
    print(s1 > 40)
    print(s1 >= 40)
    print(s1 < 40)
    print(s1 <= 40)


# function4()


def function5():
    s1 = pd.Series([10, 20, 30, 40, 50, 60], dtype=np.int8)
    print(s1)
    print(s1.index)
    print(s1.values)

    # filtering
    print(s1[s1 > 30])


function5()
