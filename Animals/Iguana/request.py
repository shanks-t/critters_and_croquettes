from datetime import date

class Iguana:

    def __init__(self, name, species, shift):
        self.date_added = date.today()
        self.home = 'glass tank'
        self.walking = True
        self.shift = shift
        self.name = name
        self.species = species