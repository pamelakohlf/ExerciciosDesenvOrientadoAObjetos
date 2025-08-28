def funcao():
  impares = []
  num = 1
  n = int(input("Digite um numero inteiro: "))
  while n > 0:
    impares.append(num)
    num += 2
    n -=1
  print(impares)

funcao()