
def nota_valida(nota):
    return 0 <= nota <= 10


trabalho = float(input("Nota do Trabalho de Laboratório (0 a 10): "))
avaliacao = float(input("Nota da Avaliação Semestral (0 a 10): "))
exame = float(input("Nota do Exame Final (0 a 10): "))


if not (nota_valida(trabalho) and nota_valida(avaliacao) and nota_valida(exame)):
    print("Erro: Todas as notas devem estar entre 0 e 10.")
else:

    media = (trabalho * 2 + avaliacao * 3 + exame * 5) / 10


    print(f"Média final: {media:.2f}")
    if media < 3:
        print("Situação: Reprovado")
    elif media < 6:
        print("Situação: Recuperação")
    else:
        print("Situação: Aprovado")
