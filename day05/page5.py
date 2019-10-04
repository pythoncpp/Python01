# set
# - collection of unique values
# - does not follow the insertion order


def function1():
    numbers = [10, 20, 30, 40, 10, 20, 30, 40]
    print(numbers)


# function1()


def function2():
    list_1 = []
    tuple_1 = ()
    dict_1 = {}
    set_1 = set()

    print(type(list_1))
    print(type(tuple_1))
    print(type(dict_1))
    print(type(set_1))


# function2()


def function3():
    # allows duplicate
    numbers_1 = [10, 20, 30, 40, 10, 20, 30, 40]
    print(numbers_1)

    # does not  allow duplicate
    numbers_2 = {10, 20, 30, 40, 10, 20, 30, 40}
    print(numbers_2)


# function3()


def function4():
    set_1 = {10, 20, 40, 20, 40, 50, 60, 70, 30, 60}
    print(set_1)

    # print(set_1[0])
    for value in set_1:
        print(value)


# function4()


def function5():
    s1 = {10, 20, 30, 40, 50}
    s2 = {40, 50, 60, 70, 80}

    print("s1 union s2 = ", s1.union(s2))
    print("s2 union s1 = ", s2.union(s1))

    print("s1 intersection s2 = ", s1.intersection(s2))
    print("s2 intersection s1 = ", s2.intersection(s1))

    print("s2 - s1 = ", (s2 - s1))
    print("s1 - s2 = ", (s1 - s2))


# function5()


def function6():
    # mutable
    set_1 = {10, 20, 30, 40, 50, 10, 20, 50}
    print(set_1)

    set_1.add(60)
    set_1.add(10)
    set_1.add(20)
    set_1.add(40)
    print(set_1)


# function6()


def function7():
    set_1 = {10, 20, 30, 40, 50, 10, 20, 50}
    print(set_1)

    # list can not be used here along with a set
    # set_1.add([10, 20])
    # set_1.add((10, 20))

    set_1.update((70, 80, 90, 10, 20, 50, 40))
    set_1.update([70, 80, 90, 10, 20, 50, 40])

    print(set_1)


# function7()


def function8():
    set_1 = {10, 20, 30, 40, 50, 10, 20, 50}
    print(set_1)

    # remove 50
    set_1.remove(50)

    # remove 20
    set_1.discard(20)

    print(set_1)

    # remove 100
    # remove will raise an exception if the value it not present in the set
    # set_1.remove(100)

    # remove 100
    # remove will NOT raise an exception if the value it not present in the set
    set_1.discard(100)

    print(set_1)


# function8()

def function9():
    names = []
    for index in range(3):
        print("enter name: ")
        name = input()
        names.append(name)

    print(names)

    # convert a list to a set
    # the duplicate values will be discarded
    unique_names = set(names)
    print(unique_names)


function9()






























