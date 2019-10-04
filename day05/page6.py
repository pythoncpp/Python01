def function1():
    person = ("person1", "person1@test.com", "pune", 59)
    print(person)

    print("name = ", person[0])


# function1()


def function2():
    # mutable
    # collection of key-value pairs
    # key has to be unique and valid (non-empty)
    person = {
         "name": "person1",
         "email": "person1@test.com",
         "address": "",
         "age": 59,
         "salary": 10.56,
         "salary": 12.56,
         "salary": 13.56,
         "salary": 15.56,
         "mobiles": ["iPhone 10 XS max", "Samsung Galaxy s10"]
    }

    # print(person)
    # print(type(person))

    print("name = ", person["name"])
    print("email = ", person["email"])
    print("address = ", person["address"])
    print("age = ", person["age"])

    print("keys: ", person.keys())
    print("values: ", person.values())

    # update the name
    person["name"] = "person2"
    print(person)

    print(person["mobiles"])
    for mobile in person["mobiles"]:
        print("person is using: ", mobile)

    print("salary = ", person["salary"])


# function2()

def function3():
    p1 = {"name": "person1", "address": "pune"}
    p2 = {"name": "person2", "address": "mumbai"}
    p3 = {"name": "person3", "address": "satara"}

    print(p1)
    print(p2)
    print(p3)


# function3()

def function4():
    # list of dictionary
    persons = [
        {"name": "person1", "address": "pune"},
        {"name": "person2", "address": "mumbai"},
        {"name": "person3", "address": "satara"}
    ]

    print(persons)

    # for person in persons:
    #     print(person)

    for person in persons:
        print("name = ", person["name"])
        print("address = ", person["address"])


function4()


