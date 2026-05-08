from .game import Game
import json
from pathlib import Path
import sqlite3

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
            return "Success"
        
    def add_to_db(self):
        conn = sqlite3.connect("games.db")
        cursor = conn.cursor()

        query = """
                    INSERT INTO games (id, title, platform, finished, rating, playtime)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """

        for game in self.library.games.values():
            print(game.title)
            cursor.execute(query, (game.id, game.title, game.platform, game.finished, game.rating, game.playtime))

        conn.commit()
        conn.close()