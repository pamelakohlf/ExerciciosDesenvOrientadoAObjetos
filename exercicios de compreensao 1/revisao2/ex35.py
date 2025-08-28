'''35. Escreva um programa que leia um numero inteiro não negativo n e imprima a soma dos n primeiros
números primos. '''

primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

n = int(input("Quantos números primos você quer somar? "))

if n > len(primos):
    print("A lista não tem tantos números primos.")
else:
    soma = sum(primos[:n]) 
    print(f"A soma dos {n} primeiros números primos é: {soma}")
