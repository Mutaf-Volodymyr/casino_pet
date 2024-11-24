from random import randint

class Table:
    def __init__(self):
        self.win_number = None

    def spin_the_wheel(self):
        self.win_number = randint(0, 36)




