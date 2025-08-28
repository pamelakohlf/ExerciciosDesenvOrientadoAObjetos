
base = int(input("Digite a base (x): "))
expoente = int(input("Digite o expoente (y): "))


resultado = 1


for _ in range(expoente):
    resultado *= base

#
print(f"\n{base}^{expoente} = {resultado}")
