from datetime import date
from .animal import Animal
from Movements import Walking, Swimming


class Turtle(Animal, Walking, Swimming):

    def __init__(self, name, species, food, chip_num):
        self.home = 'pond'
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        Swimming.__init__(self)

    def feed(self):
        print(f'{self.name} the {self.species} prefers a glass of red wine with his {self.food} each evening')

    def run(self):
        print(f'{self} does not run he walks, slowly')

    def __str__(self):
        return f'{self.name} the {self.species}'