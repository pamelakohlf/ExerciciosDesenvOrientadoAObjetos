def funcao():
  vetor = []
  for i in range(10):
    vetor.append(int(input("Digite o numero: ")))
  verifica = int(input("Digite o numero que deseja verificar: "))
  if verifica in vetor:
    print("Está no vetor")
  else:
    print("Não está no vetor")

funcao()