from .game import Game
import json
from pathlib import Path

class Storage:
    def __init__(self, library, file_path="data.json"):
        self.library = library
        self.file_path = Path(file_path)

    def load_data(self):
        game_collection = {}
        try:
            with open (self.file_path, "r") as json_file:
                data = json.load(json_file)
                #Creates a dictionary with the contents of data.json
                for game in data:
                    game_collection[game["id"]] = (Game(game["title"], game["platform"], game["finished"], game["rating"], game["playtime"], game["id"]))
            return game_collection
        except (FileNotFoundError):
            return game_collection

    def write_data(self):
        with open(self.file_path, "w") as json_file:
            #Create a list with each game as a dict for correct JSON formatting
            data = []
            for game in self.library.games.values():
                data.append(game.to_dict())
            json.dump(data, json_file, indent=4)

    def search_data(self):
        pass

    def edit_data(self):
        pass
