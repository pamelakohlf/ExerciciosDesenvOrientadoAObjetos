def funcao():
  lista = []
  while len(lista) < 10:
    lista.append(float(input("Digite o numero: ")))
  soma = sum(lista)
  print(soma)

funcao()