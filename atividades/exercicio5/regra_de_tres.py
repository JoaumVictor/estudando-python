def calculate(aValue, bValue, cValue):
    return (cValue * bValue) / aValue

def main():
    print("Regra de 3 simples")
    print("A está para B como C está para X")
    aValue = float(input("Digite o valor de A: "))
    bValue = float(input("Digite o valor de B: "))
    cValue = float(input("Digite o valor de C: "))
    result = calculate(aValue, bValue, cValue)
    print("O valor de X é ", round(result, 2))

if __name__ == "__main__":
    main()
