'''11. Considerando o intervalo de 0 a 100. Crie um programa que calcule e mostre a soma dos 50
primeiros números pares.'''
par = []

for num in range(0, 101):
    if num % 2 == 0:
        par.append(num)
        if len(par) == 50:
            break

soma = sum(par)

print(f'A soma dos 50 primeiros é de: {soma}')