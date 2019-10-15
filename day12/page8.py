class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __gt__(self, other):
        return (self._age > other._age)

    def __lt__(self, other):
        return (self._age < other._age)

    def __ge__(self, other):
        return (self._age >= other._age)

    def __le__(self, other):
        return (self._age <= other._age)

    def __eq__(self, other):
        return (self._name == other._name) and (self._age == other._age)

    def __ne__(self, other):
        return (self._name != other._name) and (self._age != other._age)


p1 = Person('person 1', 20)
p2 = Person('person 2', 40)

print('p1 > p2 = ', (p1 > p2))
print('p1 < p2 = ', (p1 < p2))
print('p1 >= p2 = ', (p1 >= p2))
print('p1 <= p2 = ', (p1 <= p2))
print('p1 == p2 = ', (p1 == p2))
print('p1 != p2 = ', (p1 != p2))