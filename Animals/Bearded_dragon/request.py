from datetime import date

class Bearded_dragon:

    def __init__(self, name, species, shift, chip_num):
        self.date_added = date.today()
        self.home = 'glass tank'
        self.walking = True
        self.shift = shift
        self.name = name
        self.species = species
        self.__chip_number = chip_num

    @property 
    def chip_number(self):
        return self.__chip_number 

    @chip_number.setter 
    def chip_number(self, number):
        pass 

