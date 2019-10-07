# list (mutable)
def function1():
    list_1 = [10, 20, 30, 40, 50]

    # add new element to the end of the list
    list_1.append(60)
    list_1.append(70)

    # remove by index
    list_1.pop(1)

    # remove by value
    list_1.remove(50)

    # reverse
    list_1.reverse()

    # sort by ascending oreder
    list_1.sort()

    # sort by descending order
    list_1.sort(reverse=True)

    # get the length of a list
    print("length - ", len(list_1))

    print(list_1)


# function1()


# tuple (immutable)
def function2():
    tuple_1 = (10, 20, 30, 40, 50)

    # get the length of a list
    print("length - ", len(tuple_1))

    # find an index of value
    print("40 appears on ", tuple_1.index(40), " index")

    # get the occurrance count
    print("50 appears ", tuple_1.count(50), " times")


# function2()


# set (mutable)
def function3():
    # duplicate values will appear only once
    set_1 = {10, 20, 30, 30, 10, 20, 40, 40, 50, 50, 50}

    print(set_1)

    # add a single value
    set_1.add(60)

    # add multiple values
    set_1.update([70, 80, 70, 80, 80, 90, 10, 20])

    print(set_1)


# function3()


# set (immutable)
def function4():
    set_1 = frozenset([10, 20, 30, 30, 10, 20, 40, 40, 50, 50, 50])

    print(set_1)

    # set_1.add(80)


# function4()


# dictionary (mutable)
def function5():
    dict_1 = {"name": "person1", "age": 40}

    print(dict_1)
    print("keys: ", dict_1.keys())
    print("values: ", dict_1.values())


function5()



















