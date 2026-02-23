import uuid

class Game:
    def __init__(self, title, platform, finished, rating=None, playtime=0.0):
        self.title = title
        self.platform = platform
        self.finished = finished
        self.rating = rating
        self.playtime = playtime
        self.id = self.create_id()

    def create_id(self):
        return uuid.uuid4()
    
    #For JSON formatting
    def to_dict(self):
        new_dict = {
            "id": str(self.id),
            "title": self.title,
            "platform": self.platform,
            "finished": self.finished,
            "rating": self.rating,
            "playtime": self.playtime
        }
        return new_dict
    
    def log_playtime(self, value):
        if value > 0:
            self.playtime += value
        else:
            print("Invalid input")
    
    def mark_finished(self):
        self.finished = True
    # Dev formatting for printing
    def __repr__(self):
        return f"Game(title={self.title!r}, platform={self.platform!r}, finished={self.finished!r}, rating={self.rating!r} playtime={self.playtime!r}, id={self.id!r})"
    # User-friendly printing
    def __str__(self):
        if self.rating == None:
            return f"Title: {self.title}, Platform: {self.platform}, Finished: {self.finished}, Playtime: {self.playtime} hrs, ID: {self.id}"
        else:
            return f"Title: {self.title}, Platform: {self.platform}, Finished: {self.finished}, Rating: {self.rating}/10, Playtime: {self.playtime} hrs, ID: {self.id}"

# zelda = Game("Zelda", "Switch", False, 8, 24.5)

# print(zelda)
# print(repr(zelda))