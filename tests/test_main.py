from src.game import Game
from src.library import Library
from src.storage import Storage

import json
from pathlib import Path
import importlib

def test_add_game(tmp_path, monkeypatch):
        #Setup
        import main
        importlib.reload(main)
        #Sets main's library and storage to temporary file path
        file_path = tmp_path / "data.json"
        main.library = Library()
        main.storage = Storage(main.library, file_path)
        #Add games to JSON
        main.library.add_game(Game("Marvel's Spider-Man 2", "PS5", True, None, 43))
        main.library.add_game(Game("Baldur's Gate 3", "Steam", True, 10, 180))
        main.storage.write_data()

        inputs = iter(["add", "The Last of Us", "PS5", "no", 5, "no"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        main.choose_action()

        with open(file_path, "r") as json_file:
                data = json.load(json_file)

        assert len(data) == 3
        assert any(game.get("title") == "The Last of Us" for game in data)
        assert any(game.get("title") == "Baldur's Gate 3" for game in data)


def test_remove_game(tmp_path, monkeypatch):
        #Setup
        import main
        importlib.reload(main)
        #Sets main's library and storage to temporary file path
        file_path = tmp_path / "data.json"
        main.library = Library()
        main.storage = Storage(main.library, file_path)
        #Add games to JSON
        main.library.add_game(Game("Marvel's Spider-Man 2", "PS5", True, None, 43))
        main.library.add_game(Game("Baldur's Gate 3", "Steam", True, 10, 180))
        main.storage.write_data()

        inputs = iter(["remove", "Blad", "Baldur's Gate 3", "no"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        main.choose_action()

        with open(file_path, "r") as json_file:
                data = json.load(json_file)

        assert len(data) == 1
        assert not any(game.get("title") == "Baldur's Gate 3" for game in data)
        assert any(game.get("title") == "Marvel's Spider-Man 2" for game in data)

def test_edit_game(tmp_path, monkeypatch):
        #Setup
        import main
        importlib.reload(main)
        #Sets main's library and storage to temporary file path
        file_path = tmp_path / "data.json"
        main.library = Library()
        main.storage = Storage(main.library, file_path)
        #Add games to JSON
        main.library.add_game(Game("Marvel's Spider-Man 2", "PS5", True, None, 43))
        main.library.add_game(Game("Baldur's Gate 3", "Steam", True, 10, 180))
        main.storage.write_data()

        inputs = iter(["edit", "Marvel's Spider-Man 2", "plat", "playtime", "56", "no"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        main.choose_action()

        with open(file_path, "r") as json_file:
                data = json.load(json_file)

        assert len(data) == 2
        assert any(game.get("playtime") == 56.0 for game in data)

        inputs = iter(["edit", "marv", "Marvel's Spider-Man 2", "fin", "finished", "False", "no"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        main.choose_action()

        with open(file_path, "r") as json_file:
                data = json.load(json_file)
        
        assert any(game.get("finished") == False for game in data)

        inputs = iter(["ed", "edit", "Baldur's Gate 3", "rating", "9", "no"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        main.choose_action()

        with open(file_path, "r") as json_file:
                data = json.load(json_file)
        
        assert any(game.get("finished") == False for game in data)
        assert any(game.get("rating") == 9 for game in data)


def test_search(tmp_path, monkeypatch):
        #Setup
        import main
        importlib.reload(main)
        #Sets main's library and storage to temporary file path
        file_path = tmp_path / "data.json"
        main.library = Library()
        main.storage = Storage(main.library, file_path)
        #Add games to JSON
        main.library.add_game(Game("Marvel's Spider-Man 2", "PS5", True, None, 43))
        main.library.add_game(Game("Baldur's Gate 3", "Steam", True, 10, 180))
        main.library.add_game(Game("Helldivers 2", "Xbox", False, 12))
        main.library.add_game(Game("Hello Kitty Island Adventure", "Switch", False, 51))
        main.storage.write_data()

        inputs = iter(["search", "all", "no"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        main.choose_action()

        with open(file_path, "r") as json_file:
                data = json.load(json_file)

        assert len(data) == 4
        assert any(game.get("title") == "Helldivers 2" for game in data)
        assert any(game.get("title") == "Marvel's Spider-Man 2" for game in data)