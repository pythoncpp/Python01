import pandas as pd


def function1():
    df = pd.read_csv('/Volumes/Data/Sunbeam/2019/August/workshops/Python01/notes/data 1/Data.csv')

    # print(df)
    # print()

    # indexing
    # print(df['Country'])

    # get all salary values
    # print(df['Salary'])

    # get salary value of 2nd employee
    # print(df['Salary'][1])

    # print(df['Salary'][2:7])
    # print(df['Salary'][:7])
    # print(df['Salary'][2:])

    # get all the values of salary with Age
    # print(df[['Salary', 'Age']])
    # print(df[['Salary', 'Age']][:])
    print(df[['Salary', 'Age']][4:])
    print(df[['Salary', 'Age']][:7])


# function1()


def function2():
    df = pd.read_csv('/Volumes/Data/Sunbeam/2019/August/workshops/Python01/notes/data 1/Data.csv')

    # print(df)

    # print(df[['Country', 'Age', 'Salary']][df['Salary'] > 60000])

    # get the salary of customers from France
    print(df['Salary'][df.Country == 'France'])

    # get the salary and age of customers from France
    print(df[['Salary', 'Age']][df.Country == 'France'])


# function2()


def function3():
    df = pd.read_csv('/Volumes/Data/Sunbeam/2019/August/workshops/Python01/notes/data 1/nba.csv')

    # print(df)
    # print(df.info())
    # print(df.describe())

    # salary
    # print(df['Salary'])
    # print(df.Salary)

    # salary > 10000000
    # print(df[['Name', 'Team', 'Salary']][df['Salary'] > 20000000])

    # salary > 1000000 or Team = 'New York Knicks'
    # print(df[['Name', 'Team', 'Salary']][(df.Salary > 100000) | (df.Team == 'New York Knicks')])
    # print(df[['Name', 'Team', 'Salary']][ (df.Salary > 100000) & (df.Team == 'New York Knicks') ])

    # convert all the float salaries into int salaries
    # df.Salary = int(df.Salary)

    # add a new column with a formula
    print(df.info())
    print()

    df['Bonus'] = df.Salary * 0.10
    print(df.info())
    print(df.head())


function3()
