from datetime import date
from .animal import Animal
from Movements import Walking


class Llama(Animal, Walking):

    def __init__(self, name, species, food, chip_num):
        self.home = 'pond'
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)

    def __str__(self):
        return f'{self.name} the {self.species}'