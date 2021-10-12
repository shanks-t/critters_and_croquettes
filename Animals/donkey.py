from datetime import date
from .animal import Animal


class Donkey:

    def __init__(self, name, species, shift):
        self.home = 'petting area'
        self.walking = True
        self.shift = shift
      