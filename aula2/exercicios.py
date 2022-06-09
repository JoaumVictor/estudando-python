# Exercício 1: Crie uma função que receba dois números e retorne o maior deles.

def maior(x, y):
    if x > y:
        print(x)
    else:
        print(y)


# maior(16, 11)

# Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.


def soma(lista):
    resultado = 0
    for numero in lista:
        resultado += numero
    print(resultado)


valores = [10, 20, 35, 5, 15, 15]

# soma(valores)

# Exercício 3: Faça um programa que, dado um valor n qualquer, tal que n > 1,
# imprima na tela um quadrado feito de asteriscos de lado de tamanho n.
# Por exemplo:


def bloco(n):
    for index in range(n):
        result = ""
        for index2 in range(n):
            result += "*"
        print(result)


def bloco2(n):
    for index in range(n):
        print("*" * n)


bloco2(5)
