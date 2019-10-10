class Player:

    def init_player(self, name, team, sport):
        self.name = name
        self.team = team
        self.sport = sport

    def print_details(self):
        print('name: ', self.name)
        print('team: ', self.team)
        print('sport: ', self.sport)
        print()


player_1 = Player()
player_1.init_player('player 1', 'india', 'cricket')
# print(player_1.__dict__)
player_1.print_details()

player_2 = Player()
player_2.init_player('player 2', 'india', 'hockey')
# print(player_2.__dict__)
player_2.print_details()

player_3 = Player()
player_3.print_details()
