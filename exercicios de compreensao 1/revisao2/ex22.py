def funcao(num):
  lista = []
  metade = num // 2
  for i in range(1, metade + 1):
    if num % i == 0:
      lista.append(i)
  print("os divisores são:",lista)
  print("A soma dos divisores do número é:",sum(lista))



num = int(input("Digite o numero: "))
funcao(num)