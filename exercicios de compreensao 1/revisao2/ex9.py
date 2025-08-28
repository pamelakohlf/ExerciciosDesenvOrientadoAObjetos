
num = float(input("Digite um número: "))
menor = maior = num


for _ in range(9):
    num = float(input("Digite um número: "))
    if num < menor:
        menor = num
    if num > maior:
        maior = num


print(f"\nMenor valor: {menor}")
print(f"Maior valor: {maior}")
