try:
    students = open('students.txt', mode="r")
    for line in students:
        x = line.split()
        if int(x[1]) < 6:
            print(f"O estudante {x[0]} está reprovado!")
        else:
            print(f"O estudante {x[0]} está aprovado!")
except OSError:
    print("Arquivo inexistente!")
else:
    print("Arquivo lido com sucesso!")
    students.close()
finally:
    print("Programa encerrado!")