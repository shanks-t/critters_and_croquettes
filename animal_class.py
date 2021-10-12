# import the python datetime module to help us create a timestamp
from datetime import date

class Llama:

    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()

miss_fuzz = Llama()
miss_fuzz.name = "Miss Fuzz"
miss_fuzz.species = "domestic Llama"


for attr, value in miss_fuzz.__dict__.items():
    print(attr, value)