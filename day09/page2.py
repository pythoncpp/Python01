# procedure oriented programming (pop)
# dict


def print_details(person):
    print("name: ", person['name'])
    print("address: ", person['address'])
    print("age: ", person['age'])
    print()


def can_vote(person):
    if person['age'] >= 18:
        print("yes.. person is eligible for voting")
    else:
        print("no.. person is NOT eligible for voting")


person_1 = {"name": "person1", "address": "pune", "age": 30}
person_2 = {"name": "person2", "address": "mumbai", "age": 10}

can_vote(person_1)
print_details(person_1)

can_vote(person_2)
print_details(person_2)


# car_1 = {'model': 'i20', 'company': 'hyundai'}
# print_details(car_1)

# empty function
def my_function():
    pass
















