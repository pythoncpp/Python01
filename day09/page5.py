class Student:
    pass


student_1 = Student()

# add an attribute to the object
student_1.name = 'student 1'
student_1.roll = 1
student_1.college = 'college 1'

print(student_1.__dict__)

print('name: ', student_1.name)
print('roll: ', student_1.roll)
print('college: ', student_1.college)


class Player:
    pass


player_1 = Player()

setattr(player_1, 'name', 'player 1')
player_1.team = 'India'

print(player_1.__dict__)

print('name: ', player_1.name)
print('team: ', getattr(player_1, 'team'))

player_2 = Player()

# add an attribute
player_2.name = "player 2"
player_2.team = "India"

print(player_2.__dict__)

# get an attribute
print("name: ", player_2.name)
print("team: ", player_2.team)

# delete an attribute
delattr(player_2, 'team')
print(player_2.__dict__)

# team doest not exist
# print("team: ", player_2.team)


