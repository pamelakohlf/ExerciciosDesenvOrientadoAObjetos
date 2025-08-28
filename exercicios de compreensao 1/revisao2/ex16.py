n = int(input("Digite um número inteiro positivo: "))

if n >= 1:
    soma = 0
    for i in range(1, n + 1):
        soma += i
    print(f"A soma dos {n} primeiros números naturais é: {soma}")
else:
    print("Número inválido. Por favor, digite um número inteiro positivo maior que zero.")
