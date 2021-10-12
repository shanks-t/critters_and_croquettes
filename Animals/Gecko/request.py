from datetime import date

class Gecko:

    def __init__(self, name, species):
        self.date_added = date.today()
        self.home = 'glass tank'
        self.walking = True
        self.name = name
        self.species = species
