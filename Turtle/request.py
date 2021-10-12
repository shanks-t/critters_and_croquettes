from datetime import date

class Turtle:

    def __init__(self, name, species):
        self.date_added = date.today()
        self.home = 'pond'
        self.walking = True
        self.swimming = True
