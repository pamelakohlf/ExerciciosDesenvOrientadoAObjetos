
quantidade = int(input("Quantos números você quer digitar? "))


if quantidade <= 0:
    print("A quantidade deve ser maior que zero.")
else:

    maior = float(input("Digite um número: "))


    for _ in range(quantidade - 1):
        num = float(input("Digite um número: "))
        if num > maior:
            maior = num


    print(f"\nO maior número digitado foi: {maior}")
