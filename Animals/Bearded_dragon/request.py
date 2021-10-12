from datetime import date
from Animals.AnimalClass import Animal

class Bearded_dragon(Animal):

    def __init__(self, name, species, food, shift, chip_num):
        super().__init__(name, species, food, chip_num)
        self.home = 'glass tank'
        self.walking = True
        self.shift = shift



