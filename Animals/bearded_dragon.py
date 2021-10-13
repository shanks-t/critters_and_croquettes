from datetime import date
from .animal import Animal
from Movements import Walking, Swimming


class Bearded_dragon(Animal, Walking, Swimming):

    def __init__(self, name, species, food, chip_num):
        self.home = 'pond'
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        Swimming.__init__(self)

    def __str__(self):
        return f'{self.name} the {self.species}'

    def feed_bearded_dragon(self):
        print(f'{self.name} the {self.species} prefers to eat his {self.food} while watching Wheel of Fortune every afternoon in his {self.home}')

