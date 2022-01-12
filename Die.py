import random

class Die:
    def __init__(self, sides=6):
        self.numSides = sides
    def roll(self):
        return random.randint(1, self.numSides)