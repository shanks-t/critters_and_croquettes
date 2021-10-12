from datetime import date
from .animal import Animal

class Bearded_dragon(Animal):

    def __init__(self, name, species, food, shift, chip_num):
        super().__init__(name, species, food, chip_num)
        self.home = 'glass tank'
        self.walking = True
        self.shift = shift

    def feed_bearded_dragon(self):
        print(f'{self.name} the {self.species} prefers to eat his {self.food} while watching Wheel of Fortune every afternoon in his {self.home}')

