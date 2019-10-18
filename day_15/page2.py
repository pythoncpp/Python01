import pandas as pd
import numpy as np


def function1():
    # list
    l1 = [10, 20, 30, 40, 50]
    print(l1)
    print()

    # array
    a1 = np.array(l1)
    print(a1)
    print()

    # series using a list
    s1 = pd.Series(l1)
    print(s1)
    # print(s1.ndim)
    # print(s1.shape)
    # print(s1.size)
    print(s1.index)
    print(s1.values)


# function1()

def function2():
    t1 = (10, 20, 30, 40, 50)

    # series using a tuple
    s1 = pd.Series(t1)
    print(s1)
    print(s1.ndim)
    print(s1.shape)
    print(s1.size)


# function2()


def function3():
    set_1 = {10, 20, 30, 40, 50, 10, 20, 30, 40, 50}
    print(set_1)

    # s1 = pd.Series(set_1)
    # print(s1)


# function3()


def function4():
    person = {'name': 'person1', 'age': 30, 'address': 'pune'}
    print(person)
    print()

    s1 = pd.Series(person)
    print(s1)
    print(s1.values)
    print(s1.index)
    print(s1.data)

    # print(int('30'))
    # print(int('test30'))


function4()
