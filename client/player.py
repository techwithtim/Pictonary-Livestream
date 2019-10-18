"""
Represents the player(s) in each game
"""


class Player(object):
    def __init__(self, name):
        self.name = name
        self.score = 0

    def update_score(self, x):
        self.score += x

    def get_score(self):
        return self.score

    def get_name(self):
        return self.name

