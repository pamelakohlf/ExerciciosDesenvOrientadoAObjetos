'''19. Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá ser
informado o número de dados lidos e número de valores pares. O processo termina quando for
digitado o número 0.'''

total = []


while True:
    num = int(input('Digite números inteiros: '))
    if num == 0:
        break
    if num % 2 == 0:
        print('Número par.')
        total.append(num)
        print(total)
    else:
        print('Número ímpar.')
        total.append(num)
        print(total)