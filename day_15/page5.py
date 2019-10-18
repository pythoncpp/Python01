import pandas as pd
import numpy as np


def function1():
    l1 = [10, 20, 30, 40, 50]
    print(l1)
    print()

    a1 = np.array(l1)
    print(a1)
    print(a1.ndim)
    print()

    s1 = pd.Series(l1)
    print(s1)
    print(s1.ndim)
    print()

    # tabular structure
    df = pd.DataFrame(l1)
    print(df)
    print(df.ndim)
    print()


# function1()


def function2():
    # person1, person1@test.com, 30, pune
    # person2, person2@test.com, 40, mumbai
    # person3, person3@test.com, 50, satara

    data = [
        {'name': 'person1', 'email': 'person1@test.com', 'age': 30, 'address': 'pune'},
        {'name': 'person2', 'email': 'person2@test.com', 'age': 40, 'address': 'mumbai'},
        {'name': 'person3', 'email': 'person3@test.com', 'age': 50, 'address': 'satara'}
    ]

    print(data)
    print(data[0])
    print(data[0]['name'])
    print(data[0]['email'])


# function2()


def function3():
    # person1, person1@test.com, 30, pune
    # person2, person2@test.com, 40, mumbai
    # person3, person3@test.com, 50, satara

    data = [
        {'name': 'person1', 'email': 'person1@test.com', 'age': 30, 'address': 'pune'},
        {'name': 'person2', 'email': 'person2@test.com', 'age': 40, 'address': 'mumbai'},
        {'name': 'person3', 'email': 'person3@test.com', 'age': 50, 'address': 'satara'}
    ]

    df = pd.DataFrame(data)
    print(df)


# function3()


def function4():
    df = pd.read_csv('/Volumes/Data/Sunbeam/2019/August/workshops/Python01/notes/data 1/Data.csv')

    print(df)


function4()