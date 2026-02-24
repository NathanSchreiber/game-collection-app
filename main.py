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
    
    def choose_platform(self):
        platform = str(input("What platform do you have this game on? "))
        if platform == "" or platform == " ":
            print("Game entries must contain a platform, please try again.")
            self.choose_platform()
        else:
            return platform
        
    def choose_finished(self):
        finished = str(input("Have you finished this game? ")).lower()
        if finished == "yes" or finished == "y":
            finished = True
        elif finished == "no" or finished == "n":
            finished = False
        else:
            print("That's not a valid response, please say yes or no." )
            self.choose_finished()

        return finished
    
    def choose_rating(self):
        rating = input("What would you rate this game 1-10? ")
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
        playtime = input("How long have you played this game in hours? ")
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
    #Combines every piece of user input to send result off to game.py
    def add_game(self):
        new_game_title = str(input("\nWhat game would you like to add? "))
        if new_game_title == "" or new_game_title == " ":
            print("Game entries must contain a title, please try again.")
            self.add_game()
        else:
            title = new_game_title
            platform = self.choose_platform()
            finished = self.choose_finished()
            rating = None
            if finished == True:
                rating = self.choose_rating()
            playtime = self.choose_playtime()
        library.add_game(Game(title, platform, finished, rating, playtime))
        storage.write_data()

class Search:
    def __init__(self):
        self.pre_sort = self.sort_alpha()

    def choose_search(self):
        search = input("What game would you like to view? Type all for entire collection - ").lower()
        if search == "all":
            self.print_sorted(self.pre_sort)
        elif search == "" or search == " ":
            print("Your search must include a valid name, please try again.")
            self.choose_search()
        else:
            search_result = ""
            fail_result = ""
            
            for _, game in self.pre_sort:
                if search == game.title.lower():
                    search_result = game
                else:
                    fail_result = "This game doesn't exist, please try again."

            if search_result != "":
                self.print_sorted(search_result)
            else:
                print(fail_result)
                self.choose_search()

    # def choose_filter(self):
    #     pass

    def sort_alpha(self, data=library.games):
        library.sort_alpha(data)
        sorted_data = library.sorted_data
        return sorted_data
    
    def sort_alpha_print(self, data=library.games):
        library.sort_alpha(data)
        sorted_data = library.sorted_data
        return sorted_data

    def print_sorted(self, data):
        print(" ")
        try:
            for _, game in data:
                print(f"{game}\n")
        except:
            print(data)


def remove_game(title):
    library.remove_game(title)
    storage.write_data()
    choose_next()
    

def choose_next():
    do_next = str(input("\nDo you want to do anything else? ")).lower()
    if do_next == "yes" or do_next == "y":
        choose_action()
    elif do_next == "no" or do_next == "n":
        pass
    else:
        print("That's not a valid response, please try again.")
        choose_next()


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
            choose_next()
        elif response1 == "search":
            search_data = Search()
            search_data.choose_search()
            choose_next()
        elif response1 == "edit":
            pass
        elif response1 == "remove":
            remove_title = str(input("What game would you like to remove? "))
            remove_game(remove_title)

            

choose_action()
