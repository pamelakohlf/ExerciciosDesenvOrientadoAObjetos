def emprestimo(salario,prestacao):
  calculo = salario * 0.2
  if prestacao > calculo:
    print("Empréstimo não concedido")
  else:
    print("Empréstimo concedido")

salario = float(input("Digite o salario: "))
prestacao = float(input("Digite o valor da prestação: "))

emprestimo(salario,prestacao)