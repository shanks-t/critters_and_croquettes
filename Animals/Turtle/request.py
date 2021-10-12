from datetime import date

class Turtle:

    def __init__(self, name, species, shift, food):
        self.date_added = date.today()
        self.home = 'pond'
        self.walking = True
        self.swimming = True
        self.shift = shift
        self.name = name
        self.species = species
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f'{self.name} is a {self.species}'