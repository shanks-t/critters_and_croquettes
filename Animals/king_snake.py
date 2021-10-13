from datetime import date

from Movements.slithering import Slithering
from .animal import Animal
from Movements import Slithering, Swimming


class King_snake(Animal, Slithering, Swimming):

    def __init__(self, name, species, food, chip_num):
        self.home = 'pond'
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)
        Swimming.__init__(self)
        
    def __str__(self):
        return f'{self.name} the {self.species}'