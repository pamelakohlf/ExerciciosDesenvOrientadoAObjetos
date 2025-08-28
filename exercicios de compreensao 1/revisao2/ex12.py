N = int(input("Digite um número inteiro positivo: "))

if N >= 0:
    print(f"Números de 0 até {N}:")
    for i in range(0, N + 1):
        print(i)
else:
    print("Número inválido. Por favor, digite um número inteiro positivo.")
