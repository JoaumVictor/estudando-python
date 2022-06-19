number = int(input("Digite um número pra ver sua tabuada:\n"))

print("===================")
for i in range(11):
    if i:
        print(f"{number} x {i} = {number * i}")
print("===================")
