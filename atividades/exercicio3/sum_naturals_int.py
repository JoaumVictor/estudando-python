numbers = input("Digite numeros naturais separados por um espaço:")

result = 0

for value in numbers.split():
    if value.isdigit() == False:
        print(f"O caractere {value} não é um número inteiro!")
    else:
        result += int(value)

print(f"A soma dos caracteres válidos deu {result}!")
