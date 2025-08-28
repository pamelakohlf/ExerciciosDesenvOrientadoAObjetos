soma_idades = 0
quantidade = 0
print("Digite as idades (digite 0 para encerrar):")
while True:
    idade = int(input(f"Idade {quantidade + 1}: "))
    
    if idade == 0:
        break
    elif idade < 0:
        print("Idade inválida. Digite um número positivo ou 0 para sair.")
        continue
    soma_idades += idade
    quantidade += 1

if quantidade > 0:
    media = soma_idades / quantidade
    print(f"\nA média das idades é: {media:.2f}")
else:
    print("\nNenhuma idade válida foi informada.")
