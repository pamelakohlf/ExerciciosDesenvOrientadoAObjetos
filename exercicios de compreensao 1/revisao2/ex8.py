soma = 0
contagem = 0
print("Digite 10 números inteiros positivos: ")

while contagem < 10:
    num = int(input(f"Digite o {contagem + 1} número: "))
    if num > 0:
        soma += num
        contagem += 1
    else:
        print("Número inválido digite apenas números inteiros positivos. ")

media = soma / 10
print(f"\nA média dos 10 números positivos é: {media}")