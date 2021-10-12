from datetime import date

class Mallard:

    def __init__(self, name, species, shift):
        self.date_added = date.today()
        self.home = 'pond'
        self.flying = True
        self.swimming = True
        self.walking = True
        self.name = name
        self.species = species