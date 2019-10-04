def function1():
    # tuple of tuples
    numbers = ((10, 20), (30, 40))

    # print(numbers)
    # print(len(numbers))

    # for row in numbers:
    #     for col in row:
    #         print(col)

    for row in range(len(numbers)):
        count = len(numbers[row])
        for col in range(count):
            print(numbers[row][col])
        print()


# function1()


def function2():
    # list of tuples
    numbers = [(10, 20), (30, 40, 50), (60, 70, 80, 90)]

    # print(numbers)

    for row in numbers:
        for value in row:
            print(value)
        print()


# function2()


def function3():
    person1 = ("person1", "person1@test.com", "+9134545", 40)
    print("name = ", person1[0])
    print("email = ", person1[1])
    print("phone = ", person1[2])
    print("age = ", person1[3])

    print()

    name, email, phone, age = ("person1", "person1@test.com", "+9134545", 40)
    print("name = ", name)
    print("email = ", email)
    print("phone = ", phone)
    print("age = ", age)


# function3()


def function4():
    persons = [
        ("person1", "person1@test.com", "+9134545", 40),
        ("person2", "person2@test.com", "+9134546", 41),
        ("person3", "person3@test.com", "+9134547", 42),
        ("person4", "person4@test.com", "+9134548", 43)
    ]

    # print(persons)

    # try 1
    # for person in persons:
    #     print(person)

    # try 2
    # for person in persons:
    #     print(person)
    #     print("name = ", person[0])
    #     print("email = ", person[1])
    #     print("phone = ", person[2])
    #     print("age = ", person[3])
    #
    #     print()

    # try 3
    # for (person) in persons:
    #     name, email, phone, age = person
    #     print("name = ", name)
    #     print("email = ", email)
    #     print("phone = ", phone)
    #     print("age = ", age)
    #
    #     print()

    # try 4
    # for name, email, phone, age in persons:
    #     print("name = ", name)
    #     print("email = ", email)
    #     print("phone = ", phone)
    #     print("age = ", age)
    #
    #     print()

    # try 5

    # for..in loop -> for..each loop
    for (name, email, phone, age) in persons:
        print("name = ", name)
        print("email = ", email)
        print("phone = ", phone)
        print("age = ", age)

        print()


# function4()


def function5():
    num = 100;
    name = 'steve'

    if num == 100:
        print("num is 100")
    else:
        print("num is not 100")

    if (num == 100):
        print("num is 100")
    else:
        print("num is not 100")

    for index in range(5):
        print(index)

    for (index) in range(5):
        print(index)
        

def function6():
    numbers = (10, 20, 30, 40, 50)

    print(numbers[0])
    print(numbers[-1])
    print(numbers[:])
    print(numbers[2:])
    print(numbers[:3])

function6()





























