num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

inicio = min(num1, num2)
fim = max(num1, num2)

soma_pares = 0
mult_imp = 1
tem_impar = False

for i in range(inicio, fim + 1):
    if i % 2 == 0:
        soma_pares += i
    else:
        mult_imp *= i
        tem_impar = True

print(f"\nSoma dos números pares entre {inicio} e {fim}: {soma_pares}")
if tem_impar:
    print(f"Multiplicação dos números ímpares entre {inicio} e {fim}: {mult_imp}")
else:
    print("Não há números ímpares no intervalo.")
