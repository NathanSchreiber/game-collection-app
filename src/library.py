from .game import Game
from .storage import Storage

class Library:
    def __init__(self):
        self.games = {}
        self.sorted_data = {}

    def load_collection(self, saved_data):
        self.games = saved_data

    def add_game(self, new_game):
        storage = Storage(new_game)
        exists_result = storage.game_exists(new_game)

        if exists_result == True:
            return "Exists"
        elif exists_result == False:
            storage.add_to_db(new_game)
            success_check = storage.game_exists(new_game)
            if success_check == True:
                return "Success"
            else:
                raise ValueError("An error occurred while adding this game")

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
        
    def edit_library(self, title, sect, new_data):
        in_list = False
        for _, game in self.games.items():
            if game.title.lower() == title.lower():
                in_list = True
                setattr(game, sect, new_data)
                return "Success"
            else:
                continue
        if in_list == False:
            return "That game doesn't exist in your library"
        
        
    def sort_alpha(self, data):
        sorted_data = sorted(data.items(), key=lambda item: item[1].title)
        self.sorted_data = sorted_data
        return self.sorted_data

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