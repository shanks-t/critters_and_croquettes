from Animals import Goat, Bearded_dragon, Buffalo, Camel, Catfish, Cobra, Crocodile, Donkey, Gecko, Goat, Iguana, King_snake, Komodo_dragon, Llama, Mallard, Turtle
from Attractions import Wetlands, PettingZoo, SnakePit

# roberto = Turtle("Roberto", "turtle", "midday", "cabbage")
# print(roberto)

# crocodile_consortium = PettingZoo("Crocodile Consortium")

# emilio = Crocodile("Emilio", "crocodile", "goat shanks")
# constatine = Crocodile("constantine", "crocodile", "tofu burgers")

# crocodile_consortium.animals.append(emilio)
# crocodile_consortium.animals.append(constatine)

# for animal in crocodile_consortium.animals:
#     print(f'you can find {animal.name} the {animal.species} in the {crocodile_consortium.attraction_name}')


# slither_inn = SnakePit("Slither Inn")
# jose = Cobra('Jose', 'cobra')
# mike = King_snake("Mike", "king Snake", "other snakes")
# dilbert = Komodo_dragon('Dilbert', 'dragon', 'cows')
# slither_inn.add_animal(mike)
# slither_inn.add_animal(dilbert)
# slither_inn.add_animal(jose)


# print(f'{slither_inn.attraction_name} is where you\'ll find reptiles of all types, like')
# for animal in slither_inn.animals:
#     print(f'-{animal.name} the {animal.species}')

# print(slither_inn.last_critter_added)

jeff = Bearded_dragon('Jeff', 'lizard', 'popcorn', 'afternoon', 999)

print(jeff.species)
print(jeff.shift)
print(jeff.chip_number)
print(jeff.feed())