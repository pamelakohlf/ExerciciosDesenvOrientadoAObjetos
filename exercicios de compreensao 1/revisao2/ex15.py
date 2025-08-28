'''15. Escreva um programa que leia um número inteiro positivo ímpar N e imprima todos os números
ímpares de 1 até N em ordem crescente. '''

numero = int(input('Digite um número inteiro positivo ímpar: '))

while numero % 2 == 0 and numero >= 0:
    numero = int(input('Digite um número inteiro positivo ímpar: '))


for cont in range(1, numero + 1, 2):
    print(cont)