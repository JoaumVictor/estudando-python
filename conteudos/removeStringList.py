gringos = ["Baianor", "Adran", "Alberto", "Diogo", "Brendin", "Bescoito"]


def findMeliante():
    name = input("Digite o nome do meliante:")
    print("Pesquisando...")
    for i, nome in enumerate(gringos):
        if str.lower(nome) == str.lower(name):
            print("=====================")
            print(f"Meliante encontrado: {nome}")
            print(f"Posição: {i}")
            print("=====================")
            return
    print(f"Meliante {name} desconhecido")


findMeliante()
