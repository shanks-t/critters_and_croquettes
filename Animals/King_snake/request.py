from datetime import date

class King_snake:

    def __init__(self, name, species, food):
        self.date_added = date.today()
        self.home = 'glass tank'
        self.slithering = True
        self.name = name
        self.species = species