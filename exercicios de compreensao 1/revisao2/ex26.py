def funcao():
  s = 0
  lista = []
  for i in range(1, 50 + 1):
    s = (2 * i - 1) / i
    lista.append(s)
  print(sum(lista))

funcao()