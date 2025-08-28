
soma = 0
quantidade = 0

print("Digite as notas (entre 0 e 10). Para sair, digite uma nota inválida.")

while True:
    nota = float(input("Nota: "))


    if 0 <= nota <= 10:
        soma += nota
        quantidade += 1
    else:
        break


if quantidade > 0:
    media = soma / quantidade
    print(f"\nMédia aritmética das notas: {media:.2f}")
else:
    print("\nNenhuma nota válida foi informada.")
