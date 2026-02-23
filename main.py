from src.game import Game
from src.library import Library
from src.storage import Storage

library = Library()
storage = Storage(library)

saved_data = storage.load_data()
library.load_collection(saved_data)


class AddGame: 
    def __init__(self):
        game = ""

    def add_game(self):
        new_game_title = str(input("\nWhat game would you like to add? "))
        if new_game_title == "":
            print("Game entries must contain a title, please try again.")
            self.add_game()
        else:
            return new_game_title
    
    def choose_platform(self):
        platform = str(input("What platform do you have this game on? "))
        if platform == "":
            print("Game entries must contain a platform, please try again.")
            self.choose_platform()
        else:
            return platform
        
    def choose_finished(self):
        finished = str(input("Have you finished this game?")).lower
        if finished == "yes":
            finished = True
        elif finished == "no":
            finished = False
        else:
            print("That's not a valid response, please say yes or no." )
            self.choose_finished()

        return finished
    
    def choose_rating(self):
        rating = input("What would you rate this game 1-10?")
        try:
            float_rating = float(rating)
        except:
            print("That isn't a valid number, please try again.")
            self.choose_rating()
        if float_rating > 10 or float_rating <= 0:
            print("Your rating must be between 1 and 10, please try again.")
            self.choose_rating()
        else:
            return float_rating
        
    def choose_playtime(self):
        playtime = input("How long have you played this game in hours?")
        try:
            float_playtime = float(playtime)
        except:
            print("That isn't a valid number, please try again.")
            self.choose_playtime()
        if float_playtime < 0:
            print("Your time played cannot be less than zero, please try again")
            self.choose_playtime()
        else:
            return float_playtime

def add_game():
    new_game_title = str(input("\nWhat game would you like to add? "))
    if new_game_title == "":
        print("Game entries must contain a title, please try again.")
        add_game()
    else:
        title = new_game_title
        def choose_platform():
            platform = str(input("What platform do you have this game on? "))
            if platform == "":
                print("Game entries must contain a platform, please try again.")
                choose_platform()
            else:
                def choose_finished():
                    finished = str(input("Have you finished this game?")).lower
                    if finished == "yes":
                        finished = True
                    elif finished == "no":
                        finished = False
                    else:
                        print("That's not a valid response, please say yes or no." )
                        choose_finished()


def remove_game(title):
    library.remove_game(title)
    storage.write_data()

print("Welcome to your game collection!\n")
print("What would you like to do?")

def choose_action():
    response1 = str(input("Add game, search game, edit game, or remove a game? ")).lower()
    if response1 != "add" and response1 != "search" and response1 != "edit" and response1 != "remove":
        print("That input was invalid, please try again.")
        choose_action()
    else:
        if response1 == "add":
            new_game = AddGame()
            new_game.add_game()
        elif response1 == "search":
            pass
        elif response1 == "edit":
            pass
        elif response1 == "remove":
            remove_title = str(input("What game would you like to remove?"))
            remove_game(remove_title)

            

choose_action()


# library.add_game(Game("The Outer Worlds", "Steam", True, None, 43))
# library.add_game(Game("Baldur's Gate 3", "Steam", True, 10, 180))


# storage.write_data()

# remove_game("The Outer Worlds")

# print(library.games)