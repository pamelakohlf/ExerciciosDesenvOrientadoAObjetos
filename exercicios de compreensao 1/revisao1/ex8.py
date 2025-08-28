
def calculo(num):
  if num >= 0:
    raiz = num ** 0.5
    print("A raiz quadrada do numero é: ",raiz)
  else:
    print("Número invalido")

num = int(input("Digite o numero: "))

calculo(num)