class Person:

    def __init__(self, name, address):
        self._name = name
        self._address = address

    def __str__(self):
        return "Person [name: {}, address: {}]".format(self._name, self._address)


def main():
    person = Person('person1', 'pune')
    print(person)

    print('page1.py: ', __name__)


# check if the the running module is page1
if __name__ == '__main__':
    main()
