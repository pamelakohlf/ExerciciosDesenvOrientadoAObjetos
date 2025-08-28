# Candidatos: 1 - JOSE ; 2 - JOAO , 3 - MARIA , 4 - ANA , 5 - Voto Nulo , 6 - Voto em Branco.

soma1 = 0
soma2 = 0
soma3 = 0
soma4 = 0
soma5 = 0
soma6 = 0

print("Códigos de votação:")
print("1 - Candidato JOSE")
print("2 - Candidato JOAO")
print("3 - Candidato MARIA")
print("4 - Candidato ANA")
print("5 - Voto Nulo")
print("6 - Voto em Branco")
print("0 - Encerrar votação")

voto = int(input("Digite o voto: "))

while voto != 0:
  if voto >= 1 and voto <= 6:
    if voto == 1:
      soma1 += 1
    elif voto == 2:
      soma2 += 1
    elif voto == 3:
      soma3 += 1
    elif voto == 4:
      soma4 += 1
    elif voto == 5:
      soma5 += 1
    elif voto == 6:
      soma6 += 1
  else:
    print("Voto invalido")
  voto = int(input("Digite o voto: "))

total_votos = soma1 + soma2 + soma3 + soma4 + soma5 + soma6

if total_votos > 0:
    votos_nulos = (soma5 * 100) / total_votos
    votos_brancos = (soma6 * 100) / total_votos
else:
    votos_nulos = 0
    votos_brancos = 0


print("\nResultado da eleição:")
print("O candidato 1 recebeu:", soma1,"votos")
print("O candidato 2 recebeu:", soma2,"votos")
print("O candidato 3 recebeu:", soma3,"votos")
print("O candidato 4 recebeu:", soma4,"votos")
print("Quantidade de votos nulos:", soma5)
print("Quantidade de votos em branco:", soma6)
print("Porcentagem de votos nulos:", votos_nulos,"%")
print("Porcentagem de votos em branco:", votos_brancos,"%")