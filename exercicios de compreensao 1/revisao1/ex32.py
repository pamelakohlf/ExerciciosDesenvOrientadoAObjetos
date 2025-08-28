def aumento(preco1):
  if preco1 < 50.00:
    preco2 = preco1 * 1.05
  elif preco1 >= 50.00 and preco1 <= 100.00:
    preco2 = preco1 * 1.10
  elif preco1 > 100.00:
    preco2 = preco1 * 1.15
  print(f"Preço novo: {preco2:.2f}")

preco1 = float(input("Digite o preço antigo: "))
aumento(preco1)

### não deu segunda tabela para cotinuar o exercicio