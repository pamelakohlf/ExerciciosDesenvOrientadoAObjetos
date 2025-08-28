def dia(num):
  semana = ["Domingo","Segunda","Terça","Quarta","Quinta","Sexta","Sabado"]
  if num >= 1 and num <= 7:
    semana = semana[num - 1]
    print("O dia da semana correspondente é:", semana)
  else:
    print("Número invalido")

num = int(input("Digite o numero: "))
dia(num)