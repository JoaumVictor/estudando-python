nome = input("Escreve um nome:")

for i, string in enumerate(list(nome)):
    print(nome[:len(nome) - i])