import tkinter as tk
from storage import Storage
from library import Library

# Not working at all, just testing how to grab things

library = Library()
storage = Storage(library)

saved_data = storage.load_data()
library.load_collection(saved_data)
library_holder = library.games.items()

print(library_holder)

for game_id, game in library_holder:
    print(game.title)

app = tk.Tk()

app.title("Game Tracker")

app.geometry("1200x800")

button = tk.Button(app, text="View Library")
button.pack(pady=300)

app.mainloop()