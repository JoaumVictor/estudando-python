import json
import random

poke_first_generation = []
with open("pokemons.json") as file:
    pokemons = json.load(file)["results"]
    for i, pokemon in enumerate(pokemons):
        poke_first_generation.append(pokemon["name"])
        if i == 151:
            break

poke_random = random.choice(poke_first_generation)
count = 1
result = ""
broken = False
while True:
    print(poke_random[:count])
    count += 1
    result = input("Quem é esse pokemon?")
    if str.lower(result) == str.lower(poke_random):
        print("Parabéns!")
        break
    if (broken):
        print("Acabaram suas chances!")
        print(f"O pokemon era o {poke_random}!")
        break
    if count == len(poke_random) - 2:
        print("Ultima chance!")
        broken = True

print("Fim de jogo!")
