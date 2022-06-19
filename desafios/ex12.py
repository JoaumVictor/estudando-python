valor = int(input("Qual o preço do produto? "))
desc = int(input("Qual o valor do desconto? "))
porcentagem = valor * desc / 100
print(f"R${valor} com {desc}% de desconto fica {valor - porcentagem}")
