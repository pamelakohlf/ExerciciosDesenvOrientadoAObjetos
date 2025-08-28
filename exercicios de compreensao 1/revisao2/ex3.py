'''3. Crie um programa que determine o mostre os 10 primeiros números pares, considerando
números maiores que 0'''

par = []

for num in range(1, 21):
    if num % 2 == 0:
        par.append(num)
        if len(par) == 10:
            break


print(f'10 primeiros num pares: {par}')