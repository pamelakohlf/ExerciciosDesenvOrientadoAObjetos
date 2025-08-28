def imc(peso,alt):
  calculo = peso / (alt * alt)
  if calculo <= 18.5:
    print("Abaixo do Peso")
  elif calculo >= 18.6 and calculo <= 24.9:
    print("Saudável")
  elif calculo >= 25.0 and calculo <= 29.9:
    print("Peso em excesso")
  elif calculo >= 30.0 and calculo <= 34.9:
    print("Obesidade Grau I")
  elif calculo >= 35.0 and calculo <= 39.9:
    print("Obesidade Grau II (severa)")
  else:
    print("Obesidade Grau III (mórbida)")

peso = float(input("Digite o peso: "))
alt = float(input("Digite a altura: "))
imc(peso,alt)