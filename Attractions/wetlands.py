from .attraction import Attraction
from Movements import walking, swimming

class Wetlands(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)

    
    def add_animal_pythonic(self, animal):
        try:
            if animal.walk_speed > -1 and animal.swim_speed > -1:
                self.animals.append(animal)
                print(f'{animal} now lives in {self.attraction_name}')
        except AttributeError as ex:
            print(f'this {animal} prefers to be in a place where it can swim and walk like {self.name}')