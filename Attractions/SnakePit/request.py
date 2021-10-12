class SnakePit:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "slithery and dithery creatures only"
        self.animals = list()
    
    def add_animal(self, animal):
        self.animals.append(animal)

    @property
    def last_critter_added(self):
        last = self.animals[-1]
        return f'{last.name}'