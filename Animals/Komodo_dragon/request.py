from datetime import date

class Komodo_dragon:

    def __init__(self, name, species, food):
        self.date_added = date.today()
        self.home = 'glass tank'
        self.walking = True
        self.name = name
        self.species = species