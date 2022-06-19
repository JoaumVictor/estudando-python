qntd = int(input("Quantas notas são:\n"))
resultado = 0
count = 1
while count <= qntd:
    value = int(input(f"Adicionar nota {count}:\n"))
    count += 1
    resultado += value
print(f"A média é {resultado / qntd}")
