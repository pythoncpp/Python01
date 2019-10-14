class Person:

    def __init__(self, name, address, age):
        self._name = name
        self._address = address
        self._age = age

    def print_person_details(self):
        print("name: ", self._name)
        print("address: ", self._address)
        print("age: ", self._age)


class Student(Person):

    def __init__(self, name, address, age, roll):
        Person.__init__(self, name, address, age)
        self._roll = roll

    def print_student_details(self):
        # call the parent class method
        Person.print_person_details(self)
        print("roll: ", self._roll)
        print()


class Player(Person):

    def __init__(self, name, address, age, team):
        Person.__init__(self, name, address, age)
        self._team = team

    def print_player_details(self):
        # calling the parent class method
        Person.print_person_details(self)
        print("team: ", self._team)
        print()


student = Student('student 1', 'pune', 20, 1)
student.print_student_details()

player = Player('player 1', 'mumbai', 30, 'india')
player.print_player_details()















