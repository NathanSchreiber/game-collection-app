from src.game import Game
from src.library import Library
from src.storage import Storage

library = Library()

library.add_game(Game("The Outer Worlds", "Steam", True, None, 43))
library.add_game(Game("Baldur's Gate 3", "Steam", True, 10, 180))

storage = Storage(library)

storage.write_data()

# print(library)

# print(library.remove_game("the outer worlds"))
# print([library])