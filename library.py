from game import Game

class Library:
    def __init__(self):
        self.games = {}

    def add_game(title, platform, finished, rating=None, playtime=0.0):
        new_game = Game(title, platform, finished, rating, float(playtime))
        return new_game


add_outer_worlds = Library.add_game("The Outer Worlds", "Steam", True, None, 43)

print(add_outer_worlds)