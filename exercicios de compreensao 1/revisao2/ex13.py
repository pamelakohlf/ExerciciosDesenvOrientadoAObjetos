# Leitura do número
n = int(input("Digite um número inteiro positivo e par: "))

# Verificação se é positivo e par
if n > 0 and n % 2 == 0:
    print(f"Números pares de 0 até {n}:")
    for i in range(0, n + 1, 2):
        print(i)
else:
    print("Erro: O número deve ser inteiro, positivo e par.")
