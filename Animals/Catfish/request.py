from datetime import date

class Catfish:

    def __init__(self, name, species):
        self.date_added = date.today()
        self.home = 'pond'
        self.swimming = True
        self.name = name
        self.species = species