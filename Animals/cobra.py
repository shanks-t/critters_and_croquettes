from datetime import date
from .animal import Animal


class Cobra(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.home = 'glass tank'
        self.slithering = True
  