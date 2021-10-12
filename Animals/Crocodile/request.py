from datetime import date

class Crocodile:

    def __init__(self, name, species, food):
        self.date_added = date.today()
        self.home = 'pond'
        self.walking = True
        self.swimming = True
        self.name = name
        self.species = species
        self.food = food