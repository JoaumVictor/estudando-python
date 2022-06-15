import random

strings = ["caminhar", "correr", "viver", "sorrir", "conhecer", "aprender"]
random_string = random.choice(strings)
scrambled_random_word = ''.join(random.sample(random_string, len(random_string)))

print(f"Que palavra é essa? {scrambled_random_word}")

resposta = ''
while resposta != random_string:
    resposta = input("Digite sua resposta: ")
    if resposta == random_string:
        print("Certa resposta!")
    else:
        print("Acho que não... kk")



