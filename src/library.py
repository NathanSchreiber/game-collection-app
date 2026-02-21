from .game import Game

class Library:
    def __init__(self):
        self.games = {}

    def add_game(self, new_game):
        if new_game.title == "":
            raise ValueError("Entered games must have a title")

        for game in self.games.values():
            if game.title.lower() == new_game.title.lower():
                raise ValueError("This game already exists in your collection")
            
        self.games[new_game.id] = new_game
        return "Game added!"

    def remove_game(self, title):
        in_list = False
        for game_id, game in self.games.items():
            if game.title.lower() == title.lower():
                in_list = True
                del self.games[game_id]
                return "Game removed!"
            else:
                continue
        if in_list == False:
            return "That game doesn't exist in your library"

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

print(library.remove_game("the outer worlds"))
print([library])