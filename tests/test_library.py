from src.library import Library
from src.game import Game
import pytest


class TestLibrary:
    def setup_method(self):
        self.library = Library()

    def test_add(self):
        new_game = Game("The Outer Worlds", "Steam", True, None, 43)
        self.library.add_game(new_game)

        stored = self.library.games[new_game.id]

        assert len(self.library.games) == 1
        assert stored.title == "The Outer Worlds"
        assert stored.platform == "Steam"
        assert stored.finished == True
        assert stored.rating == None
        assert stored.playtime == 43

        with pytest.raises(ValueError):
            fake_game = Game("", "Steam", True, 10, 180)
            self.library.add_game(fake_game)

    def test_add_duplicate_user(self):
        game1 = Game("The Outer Worlds", "Steam", True, None, 43)
        self.library.add_game(game1)

        with pytest.raises(ValueError):
            self.library.add_game(game1)


    def test_remove(self):
        game1 = Game("The Outer Worlds", "Steam", True, None, 43)
        game2 = Game("Baldur's Gate 3", "Steam", True, 10, 180)

        self.library.add_game(game1)
        self.library.add_game(game2)

        assert len(self.library.games) == 2

        self.library.remove_game("The Outer Worlds")

        assert len(self.library.games) == 1
        assert self.library.games.get(game1.id) == None
