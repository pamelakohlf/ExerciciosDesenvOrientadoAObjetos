def funcao():
  n = int(input("Digite um numero par inteiro: "))
  if n % 2 == 0:
    pares = []
    num = 0
    while n > 0:
      pares.append(num)
      num += 2
      n -=1
    pares_ordem = sorted(pares, reverse=True)
    print(pares_ordem)
  else:
    print("Número invalido")

funcao()