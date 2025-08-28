def funcao():
  num = int(input("Digite o numero: "))
  if num >= 100 and num <= 9999:
    num_str = str(num)
    lista = []
    for i in num_str:
      lista.append(i)
    print(lista)
  else:
    print("Número invalido")

funcao()