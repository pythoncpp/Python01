
def function1():
    # num = 100, name = 'steve', can_vote = True

    # multiple values assignment
    num, name, can_vote = 100, 'steve', True

    print("num = ", num)
    print("can_vote = ", can_vote)
    print("name = ", name)


# function1()


def function2():
    num1 = 10
    num2 = 20

    print("num1 = ", num1, ",  num2 = ", num2)

    # swap num1, num2
    num1, num2 = num2, num1

    print("num1 = ", num1, ",  num2 = ", num2)


# function2()


def function3():
    n1, n2, n3 = [10, 20, 30]
    print(n1)
    print(n2)
    print(n3)

    # no value for n4
    # n1, n2, n3, n4 = [10, 20, 30]

    # multiple values than number of variables
    # n4, n5 = [100, 200, 300, 400, 500]


function3()

