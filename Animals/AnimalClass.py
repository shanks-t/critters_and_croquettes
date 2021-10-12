import datetime

class Animal:
    def __init__(self, name, species, food, chip_number):
        self.name = name
        self.species = species
        self.food = food
        self.__chip_number = chip_number
        self.date_added = datetime.date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {datetime.date.today().strftime("%m/%d/%Y")}')
    
    @property
    def chip_number(self):
        return self.__chip_number
    
    @chip_number.setter
    def chip_number(self, num):
        pass
