import uuid

class Game:
    def __init__(self, title, platform, playtime=0.0):
        self.title = title
        self.platform = platform
        self.playtime = playtime
        self.id = self.create_id()

    def create_id(self):
        return uuid.uuid4()
    
    def __repr__(self):
        return f"Game(title={self.title!r}, platform={self.platform!r}, playtime={self.playtime!r} hrs, id={self.id!r})"
    
    def __str__(self):
        return f"Title: {self.title}, Platform: {self.platform}, Playtime: {self.playtime} hrs, ID: {self.id}"

zelda = Game("Zelda", "Switch", 24.5)

print(zelda)
print(repr(zelda))