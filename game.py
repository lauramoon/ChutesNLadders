from collections import defaultdict

class Game:
    """
    Class Game for a single player traversing the Chutes and Ladders board
    """
    def __init__(self):
        # number of turns to get to space 100
        self.turns = 0
        # list of spaces occupied in order
        self.moves = []
        # dictionary of game board spaces with number of times ended turn there
        self.space_map = defaultdict(int)
        # dictionary of chutes and ladders with number of times traversed
        self.cnl_map = defaultdict(int)

    def __str__(self):
        return f"Turns: {self.turns} \nCnL counts: \n{self.cnl_map}"
