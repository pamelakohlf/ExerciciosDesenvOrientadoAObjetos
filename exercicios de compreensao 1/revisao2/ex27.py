'''27. Elabore um programa que faça leitura de vários números inteiros, até que se digite um número
negativo. O programa tem que retornar o maior e o menor número lido. '''

numeros = []

while True:
    num = int(input('Digite um número inteiro: '))
    numeros.append(num)

    if num < 0:
        break

min = min(numeros)
max = max(numeros)

print(f'O número máximo é {max} e o mínimo é {min}')