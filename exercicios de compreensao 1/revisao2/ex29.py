medias = []
alunos_aprovados = 0


for i in range(1, 11):
    print(f"\nAluno {i}:")
    soma = 0
    for j in range(1, 5):
        nota = float(input(f"Digite a {j}ª nota: "))
        soma += nota
    media = soma / 4
    medias.append(media)

    if media >= 7.0:
        alunos_aprovados += 1


print(f"\nNúmero de alunos com média maior ou igual a 7.0: {alunos_aprovados}")
