from datetime import date
from .animal import Animal
from Movements import Swimming


class Catfish(Animal, Swimming):

    def __init__(self, name, species, food, chip_num):
        self.home = 'pond'
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)

    def __str__(self):
        return f'{self.name} the {self.species}'