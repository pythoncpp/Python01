class Person:
    pass


person_1 = Person()
setattr(person_1, 'name', 'person 1')
setattr(person_1, 'address', 'pune')

print(person_1.__dict__)


person_2 = Person()
person_2.full_name = 'person2 person2'
person_2.full_address = 'mumbai'
person_2.phone = "+9123433242424"

print(person_2.__dict__)
