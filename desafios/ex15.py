days = int(input("Quantos dias alugado?"))
km = float(input("Quantos km rodados?"))
km_value = 0.15
day_value = 60
resultado = days * day_value + km * km_value
print(f"Deu R${resultado}")
