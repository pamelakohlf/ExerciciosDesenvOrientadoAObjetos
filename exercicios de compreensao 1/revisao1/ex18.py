numero = int(input("Digite um número inteiro maior que zero: "))

if numero <= 0:
    print("Número inválido")
else:
    soma = 0
    for digito in str(numero):
        soma += int(digito)
    print("A soma dos algarismos é:", soma)
