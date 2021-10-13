from datetime import date
from .animal import Animal
from Movements import Walking, Swimming


class Iguana(Animal, Walking, Swimming):

    def __init__(self, name, species, food, chip_num):
        self.home = 'pond'
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        Swimming.__init__(self)