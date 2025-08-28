'''Faça um Programa que leia 20 números inteiros e armazene-os em uma LISTA. Armazene os
números pares na lista PAR e os números IMPARES na lista ímpar. Imprima os três vetores. '''

par = []
impar =[]
todos = []


for num in range(1,21):
    numeros = int(input('Digite um número: '))
    todos.append(numeros)
    if numeros % 2 == 0:
        par.append(numeros)
    else:
        impar.append(numeros)

print(f'Números {todos}\nPares {par}\nímpar:{impar}')