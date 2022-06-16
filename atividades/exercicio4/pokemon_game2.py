import json
import random

poke_first_generation = []
with open("pokemons.json") as file:
    pokemons = json.load(file)["results"]
    for i, pokemon in enumerate(pokemons):
        poke_first_generation.append(pokemon["name"])
        if i == 151:
            break

# with open("pokemons.json") as file:
# poke_first_generation = [pokemon["name"] for pokemon in pokemons[:151]]

points = 0
finish = False
round = 1


def generate_poke_random():
    return random.choice(poke_first_generation)


def message_round():
    global round
    if round == 5:
        print("Uma Fera! 🔥")
    if round == 10:
        print("Uma Máquina! 🔥")
    if round == 15:
        print("Uma Lenda! 🔥")


def run_game():
    global points, finish, round
    count = 1
    result = ""
    broken = False
    poke_random = generate_poke_random()
    print("===================================")
    print(f"Rodada: {round} / Pontuação: {points}")
    message_round()
    while count != len(poke_random) - 1:
        print(poke_random[:count], "_" * (len(poke_random) - len(poke_random[:count])))
        count += 1
        result = input("Quem é esse pokemon? 🧐\n")
        if str.lower(result) == str.lower(poke_random):
            print("Parabéns!")
            broken = False
            points += (len(poke_random) - len(poke_random[:count]) + 1)
            break
        if count == len(poke_random) - 2:
            print("Ultima chance!")
            broken = True
    if broken:
        finish = True
        print("Acabaram suas chances!")
        print(f"O pokemon era o {poke_random}!")
    print("Fim de round!")
    round += 1
    print("===================================")

run_game()


while True:
    if finish:
        print(f"Você fez {points} pontos!")
        break
    print(f"Você tem {points} pontos!")
    answer_continue = input("Deseja continuar? (Y/n)")
    if str.lower(answer_continue) == "y" or str.lower(answer_continue) == '':
        run_game()
    else:
        break


print("Fim de jogo!")
