import json
from pathlib import Path

class Storage:
    def __init__(self, library, file_path="data.json"):
        self.library = library
        self.file_path = Path(file_path)

    def write_data(self):
        with open(self.file_path, "w") as json_file:
            #Create a list with each game as a dict for correct JSON formatting
            data = []
            for game in self.library.games.values():
                data.append(game.to_dict())
            json.dump(data, json_file, indent=4)

    def read_data(self):
        pass

    def edit_data(self):
        pass

    def remove_data(self):
        pass