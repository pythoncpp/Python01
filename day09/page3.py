# class
# - template/blueprint to create an object

# object
# - instance of a class
# - the real memory block where the attributes and methods get stored
# - unit of collection of
#   - attributes
#     - those which will store information
#     - e.g. name, age, address are attributes of person
#     - e.g. model, company, price are attributes of car
#   - methods
#     - function inside a class
#     - e.g. can_vote, print_details are the methods of person
#     - e.g. print_details, can_afford are the methods of car


# empty class
class Person:
    pass


# object of Person
person = Person()

# print(type(Person))
print(type(person))
print(person)

# convert the object to dictionary of attributes/methods
print(person.__dict__)













