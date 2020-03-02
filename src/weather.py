from random import random

class Weather:
    def is_stormy(self):
        roll = random()
        if roll > 0.75:
            return False
        return True
