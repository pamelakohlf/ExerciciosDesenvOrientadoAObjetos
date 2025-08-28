def taxa(valor,estado):
  if estado == "MG":
    preco = valor + (valor * 0.07)
  elif estado == "SP":
    preco = valor + (valor * 0.12)
  elif estado == "RJ":
    preco = valor + (valor * 0.15)
  elif estado == "MS":
    preco = valor + (valor * 0.08)
  else:
    return "Estado invalido"
  return preco

valor = float(input("Digite o valor do produto: "))
estado = str(input("Digite o Estado: "))

resultado = taxa(valor,estado)
print(resultado)