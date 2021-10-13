from .attraction import Attraction
from Movements import slithering


class SnakePit(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)


    # Snake Typing Check the python way
    def add_animal_pythonic(self, animal):
        try:
            if animal.slither_speed > -1:
                self.animals.append(animal)
                print(f'{animal} now lives in {self.attraction_name}')
        except AttributeError as ex:
            print(f'this {animal} loves to slither and prefers to be with other slithery creatures in the {self.name}')


    