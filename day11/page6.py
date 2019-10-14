class Person:

    def __init__(self):
        # protected
        self._name = 'person1'
        self._address = 'pune'

    def print_person_details(self):
        print('name: ', self._name)
        print('address: ', self._address)


class Player(Person):

    def __init__(self):
        Person.__init__(self)

        # private
        self.__team = 'india'

    def print_player_details(self):
        print("name: ", self._name)
        print("address: ", self._address)
        print("team: ", self.__team)


player1 = Player()
# player1.name = 'corrupted'
# player1._name = "corrupted"
player1.print_player_details()
