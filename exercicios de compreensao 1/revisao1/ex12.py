def funcao(num1,num2):
  if num1 == num2:
    print("Números iguais")
  elif num1 > num2:
    diferenca = num1 - num2
    print("Numero maior:", num1)
    print("Diferença entre os numeros:",diferenca)
  else:
    diferenca = num1 - num2
    print("Numero maior:", num2)
    print("Diferença entre os numeros:",diferenca)

num1 = int(input("Digite o numero: "))
num2 = int(input("Digite o outro numero: "))

funcao(num1,num2)