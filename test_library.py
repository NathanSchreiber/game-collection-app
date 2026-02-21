from library import Library
from game import Game
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

    def test_add_duplicate_user(self):
        game1 = Game("The Outer Worlds", "Steam", True, None, 43)
        self.library.add_game(game1)

        with pytest.raises(ValueError):
            self.library.add_game(game1)


    # def test_remove(self):
    #     g1 = Game("The Outer Worlds", "Steam", True, None, 43)
    #     g2 = Game("Baldur's Gate 3", "Steam", True, 10, 180)

    #     self.library.add_game(g1)
    #     self.library.add_game(g2)

    #     assert len(self.library.games) == 2

    #     self.library.remove_game("The Outer Worlds")
    #     # Broken ->
    #     removed = self.library.games[g1.id]

    #     print(removed.title)

    #     self.assertNotIn(removed)
    #     # <- Broken
