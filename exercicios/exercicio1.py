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


# bloco2(5)

# Exercício 4: Crie uma função que receba uma lista de nomes e retorne o nome com a maior quantidade de
#  caracteres. Por exemplo, para ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"], o retorno deve
#  ser "Fernanda".

def findbiggestword(array):
    resultado = ""
    for palavra in array:
        if len(palavra) > len(resultado):
            resultado = palavra
    print(resultado)

nomes = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Victor"]
# findbiggestword(nomes)


# Exercício 5: Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é
# vendida em latas de 18 litros, que custam R$ 80,00. Crie uma função que retorne dois valores em uma tupla 
# contendo a quantidade de latas de tinta a serem compradas e o preço total a partir do tamanho de uma 
# parede(em m²).

# 1 lata = 54 metros = R$80

def calculateInk(meters):
    lata = 1
    metros = 54
    valorLata = 80
    lataQt = round((meters * lata / metros), 2)
    valorFinal = round((lataQt * valorLata / lata), 2)
    print(f"Você vai precisar de {lataQt} latas, que dá R${valorFinal}!")

# calculateInk(70)

#Exercício 6: Crie uma função que receba os três lado de um triângulo e informe qual o tipo de triângulo
# formado ou "não é triangulo", caso não seja possível formar um triângulo.

def informTriangleType(v1, v2, v3):
    erro = "Isso não é um triângulo!"
    if(v1 + v2 > v3):
        if(v1 + v3 > v2):
            if(v2 + v3 > v1):
                if(v1 == v2 and v2 == v3):
                    return print("Triângulo Equilátero: três lados iguais!")
                elif(v1 == v2 or v2 == v3 or v1 == v3):
                    return print("Triângulo Isósceles: quaisquer dois lados iguais!")
                else:
                    return print("Triângulo Escaleno: três lados diferentes.")
            print("erro no terceiro if")
        print("erro no segundo if")
    print(erro)

# informTriangleType(6, 3, 8)