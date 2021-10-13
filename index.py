from Animals import goat, Bearded_dragon, Buffalo, Camel, Catfish, Cobra, Crocodile, Donkey, Gecko, Goat, Iguana, King_snake, Llama, Turtle, Mallard, Falcon
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


slither_inn = SnakePit("Slither Inn", "we cold-blooded over here")
jose = Cobra('Jose', 'cobra', 'spaghetti', 666)
mike = King_snake("Mike", "king Snake", "other snakes", 777)


slither_inn.add_animal_pythonic(mike)
slither_inn.add_animal_pythonic(jose)


print(f'{slither_inn.attraction_name} is where you\'ll find snakes of all types, like')
for animal in slither_inn.animals:
    print(animal)

print(slither_inn.last_critter_added)


marsh_motel = Wetlands("Marsh Motel", "bring your boots, it's mucky out there")
flocculent_fortress = PettingZoo("Flocculent Fortress", "If you ain\'t got fur you don't belong")

cassie = Turtle('Cassie', 'box turtle', 'veggie pizza', 800 )
cameron = Crocodile('Cameron', 'crocodile', 'california roll', 544)

marsh_motel.add_animal_pythonic(cassie)
marsh_motel.add_animal_pythonic(cameron)
flocculent_fortress.add_animal_pythonic(cameron)



print(f'-{marsh_motel.attraction_name} is where all the swampy creatures hang out, like')
for animal in marsh_motel.animals:
    print(f'-{animal.name} the {animal.species}')