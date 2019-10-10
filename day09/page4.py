class Person:
    pass


# person: reference to an object
# Person: class
person = Person()
print(person.__dict__)

# add/set the attributes
setattr(person, 'name', 'person1')
setattr(person, 'address', 'pune')
setattr(person, 'age', 30)

print(person.__dict__)

# get the attribute values
print("name: ", getattr(person, 'name'))
print("address: ", getattr(person, 'address'))
print("age: ", getattr(person, 'age'))


class Car:
    pass


car_1 = Car()

setattr(car_1, 'model', 'i20')
setattr(car_1, 'company', 'hyundai')
setattr(car_1, 'price', 7.5)

print('model: ', getattr(car_1, 'model'))
print('company: ', getattr(car_1, 'company'))
print('price: ', getattr(car_1, 'price'))


car_2 = Car()

setattr(car_2, 'model', 'nano')
setattr(car_2, 'company', 'tata')
setattr(car_2, 'price', 2.5)

print('model: ', getattr(car_2, 'model'))
print('company: ', getattr(car_2, 'company'))
print('price: ', getattr(car_2, 'price'))



