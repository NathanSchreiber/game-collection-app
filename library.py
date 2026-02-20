from game import Game

class Library:
    def __init__(self):
        self.games = {}
        self.id_list = []

    def add_game(self, new_game):
        self.games[new_game.id] = new_game
        self.id_list.append(new_game.id)
        return "Game added!"

    def remove_game(self, game_id):
        if game_id in self.games:
            del self.games[game_id]
            return "Game removed!"
        else:
            return("That game doesn't exist in your library")

    def __repr__(self):
        return str(self.games)
    
    def __str__(self):
        print_game_list = ""
        for game in self.games:
            entry = self.games[game]
            if entry.rating == None:
                print_game = f"Title: {entry.title}, Platform: {entry.platform}, Finished: {entry.finished}, Playtime: {entry.playtime} hrs, ID: {entry.id}"
                print_game_list += f"{print_game}\n"
            else:
                print_game = f"Title: {entry.title}, Platform: {entry.platform}, Finished: {entry.finished}, Rating: {entry.rating}/10, Playtime: {entry.playtime} hrs, ID: {entry.id}"
                print_game_list += f"{print_game}\n"
        return str(print_game_list)


library = Library()

library.add_game(Game("The Outer Worlds", "Steam", True, None, 43))
library.add_game(Game("Baldur's Gate 3", "Steam", True, 10, 180))

print(library)

library.remove_game(library.id_list[0])
print(library)