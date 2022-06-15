import random

file = open("strings_game.txt", mode="r")
fruits = []
for line in file:
    fruits.append(line[:len(line) - 1])
file.close()

random_fruit = random.choice(fruits)
scrambled_random_fruit = ''.join(random.sample(
    random_fruit, len(random_fruit)))

print(f"Que fruta é essa? {scrambled_random_fruit}")

resposta = ''
while resposta != random_fruit:
    resposta = input("Digite sua resposta: ")
    if resposta == random_fruit:
        print("Certa resposta!")
    else:
        print("Acho que não... kk")
