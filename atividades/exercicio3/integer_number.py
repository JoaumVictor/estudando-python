while True:
    try:
        x = int(input("Digite um número inteiro: "))
        break
    except ValueError:
        print("Ué, isso não foi um número inteiro, tente de novo...")
        