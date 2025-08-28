maior_idade = 0
maior_altura = 0
maior_peso = 0
soma_altura = 0
soma_imc = 0
qtd_masculino = 0
qtd_feminino = 0

for i in range(1, 26):
    print(f"\nPessoa {i}:")
    
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").strip().upper()
    altura = float(input("Altura (em metros): "))
    peso = float(input("Peso (em kg): "))

    if idade > maior_idade:
        maior_idade = idade

    if altura > maior_altura:
        maior_altura = altura

    if peso > maior_peso:
        maior_peso = peso

    soma_altura += altura
    imc = peso / (altura ** 2)
    soma_imc += imc

    if sexo == 'M':
        qtd_masculino += 1
    elif sexo == 'F':
        qtd_feminino += 1

media_altura = soma_altura / 25
media_imc = soma_imc / 25
porcentagem_masculino = (qtd_masculino / 25) * 100
porcentagem_feminino = (qtd_feminino / 25) * 100

print("\n--- Resultados Finais ---")
print("Idade da pessoa mais velha:", maior_idade)
print("Altura da pessoa mais alta:", maior_altura)
print("Maior peso:", maior_peso)
print(f"Média de altura: {media_altura:.2f} m")
print(f"Média de IMC: {media_imc:.2f}")
print(f"Porcentagem de sexo masculino: {porcentagem_masculino:.1f}%")
print(f"Porcentagem de sexo feminino: {porcentagem_feminino:.1f}%")
