from src.game import Game
from src.library import Library
from src.storage import Storage
import json
from pathlib import Path

class TestStorage:
    def test_write_data(self, tmp_path):
        #Setup
        library = Library()
        file_path = tmp_path / "data.json"
        storage = Storage(library, file_path)
        #Add games to JSON
        library.add_game(Game("Marvel's Spider-Man 2", "Playstation 5", True, None, 43))
        library.add_game(Game("Baldur's Gate 3", "Steam", True, 10, 180))
        storage.write_data()
        #Open and check JSON
        with open(file_path, "r") as json_file:
            data = json.load(json_file)

        assert len(data) == 2

        by_title = {game["title"]: game for game in data}

        spider_man = by_title["Marvel's Spider-Man 2"]
        bg3 = by_title["Baldur's Gate 3"]

        assert "id" in spider_man
        assert spider_man["title"] == "Marvel's Spider-Man 2"
        assert spider_man["platform"] == "Playstation 5"
        assert spider_man["finished"] is True
        assert spider_man["rating"] is None
        assert spider_man["playtime"] == 43

        assert "id" in bg3
        assert bg3["title"] == "Baldur's Gate 3"
        assert bg3["platform"] == "Steam"
        assert bg3["finished"] is True
        assert bg3["rating"] == 10
        assert bg3["playtime"] == 180

    def test_load_data(self, tmp_path):
        #Setup
        library = Library()
        file_path = tmp_path / "data.json"
        storage = Storage(library, file_path)
        #Add games to JSON
        library.add_game(Game("Marvel's Spider-Man 2", "Playstation 5", True, None, 43))
        library.add_game(Game("Baldur's Gate 3", "Steam", True, 10, 180))
        storage.write_data()

        #Test loading converted data
        stored_data = storage.load_data()
        print(stored_data)
        assert type(stored_data) == dict
        
        for game in stored_data.values():
            assert game.id != None
            assert type(game) != dict
            if game.title == "Marvel's Spider-Man 2":
                assert game.title == "Marvel's Spider-Man 2"
                assert game.platform == "Playstation 5"
                assert game.finished is True
                assert game.rating is None
                assert game.playtime == 43
            else:
                assert game.title == "Baldur's Gate 3"
                assert game.platform == "Steam"
                assert game.finished is True
                assert game.rating == 10
                assert game.playtime == 180