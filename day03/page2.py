# parameterless function
def function1():
    print("inside function1")

# function1()


# parameterized function
def function2(param1):
    print("inside function2")
    print("param1 = ", param1)
    print("type of param1 = ", type(param1))


# function2(10)
# function2(10.56)
# function2('test')
# function2(True)


def add(p1, p2):
    print("p1 = ", p1)
    print("p2 = ", p2)
    result = p1 + p2
    print("result = ", result)


# calling function with param values
# add(10, 30)

# calling function with param value and its name
# named parameters
# add(p1=10, p2=30)
# add(p2=30, p1=10)


def print_person_details(name, address, phone, email):
    print("name = ", name)
    print("address = ", address)
    print("phone = ", phone)
    print("email = ", email)


# print_person_details("person1", "pune", "person1@test.com", "+913453345")
# print_person_details(name="person1", email="person1@test.com", phone="+913453354", address="Pune")


# default parameter value or optional parameter
# p2 will use the default value = 1
# if value of p2 is missing then use p2 = 1
# if value of p2 is available then use the parameter value
def multiply(p1, p2=1):
    print("p1 = ", p1)
    print("p2 = ", p2)
    result = p1 * p2
    print("result = ", result)


# multiply(10, 40)
# multiply(p2=40, p1=10)

# multiply(40)
# multiply(40, 80)


def add_1(p1=0, p2=0):
    print("p1 = ", p1)
    print("p2 = ", p2)
    result = p1 + p2
    print("result = ", result)


# add_1(10, 20)
# add_1(10)
# add_1(p2=40)
# add_1(10.56, 40.50)
# add_1()
