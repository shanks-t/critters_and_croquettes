from .attraction import Attraction
from Movements import walking

class PettingZoo(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)
    
    def add_animal_pythonic(self, animal): 
        if animal.walk_speed > -1 and not animal.species == 'crocodile':
            self.animals.append(animal)
            print(f'{animal} now lives in {self.attraction_name}')
        else:
            print(f'{animal} doesn\'t like to be petted, so please do not put it in the {self.attraction_name} attraction.')