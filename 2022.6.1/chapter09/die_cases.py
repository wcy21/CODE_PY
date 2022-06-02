from random import randint


class Die():
    """骰子类"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        side = randint(1, 6)
        print(side)


die1 = Die(6)
print("\nThe result of ten rolls of a 6-sided die:")
for i in range(10):
    die1.roll_die()

die2 = Die(10)
print("\nThe result of ten rolls of a 10-sided die:")
for i in range(10):
    die2.roll_die()

die3 = Die(20)
print("\nThe result of ten rolls of a 20-sided die:")
for i in range(10):
    die2.roll_die()
