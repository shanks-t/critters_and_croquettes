from datetime import date

class Llama:

    def __init__(self, name, species, shift):
        self.date_added = date.today()
        self.home = 'petting area'
        self.walking = True
        self.shift = shift
        self.name = name
        self.species = species