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
            return self.choose_platform()
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
            return self.choose_finished()

        return finished
    
    def choose_rating(self):
        rating = input("What would you rate this game 1-10? ")
        try:
            float_rating = float(rating)
        except:
            print("That isn't a valid number, please try again.")
            return self.choose_rating()
        if float_rating > 10 or float_rating <= 0:
            print("Your rating must be between 1 and 10, please try again.")
            return self.choose_rating()
        else:
            return float_rating
        
    def choose_playtime(self):
        playtime = input("How long have you played this game in hours? ")
        try:
            float_playtime = float(playtime)
        except:
            print("That isn't a valid number, please try again.")
            return self.choose_playtime()
        if float_playtime < 0:
            print("Your time played cannot be less than zero, please try again")
            return self.choose_playtime()
        else:
            return float_playtime
    #Combines every piece of user input to send result off to game.py
    def add_game(self):
        new_game_title = str(input("\nWhat game would you like to add? "))
        if new_game_title == "" or new_game_title == " ":
            print("Game entries must contain a title, please try again.")
            return self.add_game()
        else:
            title = new_game_title
            platform = self.choose_platform()
            finished = self.choose_finished()
            rating = None
            if finished == True:
                rating = self.choose_rating()
            playtime = self.choose_playtime()
        library.add_game(Game(title, platform, finished, rating, playtime))
        success_test = storage.write_data()
        if success_test == "Success":
            print("Game added!")
        else:
            print("Error")

class Search:
    def __init__(self):
        #Sorts the data before it's called
        self.pre_sort = self.sort_alpha()

    def choose_search(self):
        search = str(input("What game would you like to view? Type all for entire collection - ")).lower()
        if search == "all":
            self.print_sorted(self.pre_sort)
        elif search == "" or search == " ":
            print("Your search must include a valid name, please try again.")
            return self.choose_search()
        else:
            search_result = ""
            fail_result = "This game doesn't exist, please try again."
            
            for _, game in self.pre_sort:
                if search == game.title.lower():
                    search_result = game
                    break
                else:
                    continue

            if search_result != "":
                self.print_sorted(search_result)
            else:
                print(fail_result)
                return self.choose_search()

    def sort_alpha(self, data=None):
        if data == None:
            data = library.games
        library.sort_alpha(data)
        sorted_data = library.sorted_data
        return sorted_data
    
    def sort_alpha_print(self, data=None):
        if data == None:
            data = library.games
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

class Edit:
    def __init__(self):
        self.pre_sort = ""
        self.sort_tools = ""

    def add_sort_tools(self):
        sort_tools = Search()
        self.sort_tools = sort_tools
        self.pre_sort = sort_tools.sort_alpha()

    def choose_game(self):
        def choose_sect():
            edit_sect = str(input("What section would you like to edit? ")).lower()
            if edit_sect != "title" and edit_sect != "platform" and edit_sect != "finished" and edit_sect != "rating" and edit_sect != "playtime":
                print("Section must be Title, Platform, Finished, Rating, or Playtime. Please try again.")
                return choose_sect()
            else:
                return edit_sect
            
        def replace_data(sect):
            new_data = str(input("What would you like to replace the current data with? ")).lower()
            if sect == "finished":
                if new_data == "yes" or new_data == "y" or new_data == True:
                    new_data = True
                    return new_data
                elif new_data == "no" or new_data == "n" or new_data == False:
                    new_data = False
                    return new_data
                else:
                    print("This response must be True, False, yes, or no. Please try again.")
                    return replace_data(sect)
            elif sect == "rating" or sect == "playtime":
                try:
                    float_data = float(new_data)
                    if sect == "rating":
                        if float_data < 1 or float_data > 10:
                            print("Rating must be between 1 and 10, please try again?")
                            return replace_data(sect)
                        else:
                            return float_data
                    else:
                        if float_data < 0:
                            print("Playtime must be 0 or greater, please try again?")
                            return replace_data(sect)
                        else:
                            return float_data
                except:
                    print("This data must be a number, please try again.")
                    return replace_data(sect)
            else:
                if new_data == "" or new_data == " ":
                    print("Input cannot be empty, please try again.")
                    return replace_data(sect)
                else:
                    return new_data


        search = str(input("What game would you like to edit? ")).lower()
        if search == "" or search == " ":
            print("Your search must include a valid name, please try again.")
            return self.choose_game()
        else:
            search_result = ""
            fail_result = "This game doesn't exist, please try again."
            
            for _, game in self.pre_sort:
                if search == game.title.lower():
                    search_result = game
                    self.sort_tools.print_sorted(game)
                    edit_sect = choose_sect()
                    new_data = replace_data(edit_sect)
                    library.edit_library(game.title, edit_sect, new_data)
                    check_success = storage.write_data()
                    if check_success == "Success":
                        print("Game Updated!")
                    break
                else:
                    continue

            if search_result != "":
                pass
            else:
                print(fail_result)
                return self.choose_game()


class Remove:
    def __init__(self):
        self.pre_sort = ""
        self.sort_tools = ""

    def add_sort_tools(self):
        sort_tools = Search()
        self.sort_tools = sort_tools
        self.pre_sort = sort_tools.sort_alpha()

    def remove_game(self):
        remove_title = str(input("What game would you like to remove? ")).lower()

        if remove_title == "" or remove_title == " ":
            print("Your search must include a valid name, please try again.")
            return self.remove_game()
        else:
            search_result = ""
            fail_result = "This game doesn't exist, please try again."
            
            for _, game in self.pre_sort:
                if remove_title == game.title.lower():
                    search_result = game
                    self.sort_tools.print_sorted(game)
                    library.remove_game(remove_title)
                    check_success = storage.write_data()
                    if check_success == "Success":
                        print("Game Updated!")
                    else:
                        print("Error")
                    break
                else:
                    continue

            if search_result != "":
                pass
            else:
                print(fail_result)
                return self.remove_game()

    

def choose_next():
    do_next = str(input("\nDo you want to do anything else? ")).lower()
    if do_next == "yes" or do_next == "y":
        return choose_action()
    elif do_next == "no" or do_next == "n":
        pass
    else:
        print("That's not a valid response, please try again.")
        return choose_next()


def choose_action():
    response1 = str(input("Add game, search game, edit game, or remove a game? ")).lower()
    if response1 != "add" and response1 != "search" and response1 != "edit" and response1 != "remove":
        print("That input was invalid, please try again.")
        return choose_action()
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
            new_edit = Edit()
            new_edit.add_sort_tools()
            new_edit.choose_game()
        elif response1 == "remove":
            remove = Remove()
            remove.add_sort_tools()
            remove.remove_game()
            choose_next()

            
def main():
    print("Welcome to your game collection!\n")
    print("What would you like to do?")

    choose_action()

#Only run when main.py is executed directly
if __name__ == "__main__":
    main()
