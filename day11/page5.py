class Person:

    def __init__(self):
        # public
        self.name = 'person1'
        self.address = 'pune'

    def print_person_details(self):
        print('name: ', self.name)
        print('address: ', self.address)


class Player(Person):

    def __init__(self):
        Person.__init__(self)
        self.team = 'india'

    def print_player_details(self):
        print("name: ", self.name)
        print("address: ", self.address)
        print("team: ", self.team)


player1 = Player()
player1.name = 'corrupted'
player1.print_player_details()
