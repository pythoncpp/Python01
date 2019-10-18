import pandas as pd
import numpy as np


def function1():
    emails = pd.Series(['person1@test.com', 'person2@test.com', 'person2@test.com'])
    print(emails)

    print(emails[0])


# function1()


def function2():
    persons = ['person1', 'person2', 'person3']
    emails = ['person1@test.com', 'person2@test.com', 'person2@test.com']

    email_series = pd.Series(emails, index=persons)
    print(email_series)

    # indexing
    print(email_series['person1'])
    print(email_series['person2'])
    print(email_series['person3'])

    print(email_series.values)
    print(email_series.index)


# function2()


def function3():
    mileages = [21, 20, 23, 25, 27]
    models = ['i10', 'nano', 'i20', 'fortuner', 'x5']

    s1 = pd.Series(mileages)
    print(s1)
    print(s1[2])
    print()

    s2 = pd.Series(models)
    print(s2)
    print(s2[3])
    print()

    s3 = pd.Series(mileages, index=models)
    print(s3)
    print(s3['i20'])
    print(s3.index)
    print(s3.values)
    print()

    s4 = pd.Series(models, index=mileages)
    print(s4)
    print(s4[27])
    print(s4.index)
    print(s4.values)
    print()


function3()