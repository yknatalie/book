from random import randint
from random import choice


class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


# six = Die()
#  six.roll_die()
# ten = Die(10)
# ten.roll_die()
# twenty = Die(20)
# twenty.roll_die()
lottery = (1, 3, 34, 24, 67, 345, 21, 4, 2, 8, 'f', 'd', 't', 'w', 'r')
first = choice(lottery)
second = choice(lottery)
third = choice(lottery)
fourth = choice(lottery)
# print(
#     f' A Person who has combination of these numbers is the winner:{first} {second} {third} {fourth}')
win_combination = [3, 345, 4, 67]
my_ticket = []
iterator = 0
while True:
    my_ticket.append(choice(lottery))
    my_ticket.append(choice(lottery))
    my_ticket.append(choice(lottery))
    my_ticket.append(choice(lottery))
    iterator += 1
    if my_ticket == win_combination:
        print(iterator)
        break
    else:
        my_ticket.clear()
