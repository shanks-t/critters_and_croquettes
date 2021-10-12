from datetime import date

class Cobra:

    def __init__(self, name, species):
        self.date_added = date.today()
        self.home = 'glass tank'
        self.slithering = True
        self.name = name
        self.species = species