class Triangulo:
  def __init__(self,ladoA,ladoB,ladoC):
    self.ladoA = ladoA
    self.ladoB = ladoB
    self.ladoC = ladoC

  def calcularPerimetro(self):
    return self.ladoA + self.ladoB + self.ladoC

  def getMaiorLado(self):
    if self.ladoA >= self.ladoB and self.ladoA >= self.ladoC:
      return self.ladoA
    elif self.ladoB >= self.ladoA and self.ladoB >= self.ladoC:
      return self.ladoB
    else:
      return self.ladoC

  def equilatero(self):
    if self.ladoA == self.ladoB and self.ladoA == self.ladoC:
      return True

  def isosceles(self):
    if self.ladoA == self.ladoB and self.ladoA != self.ladoC:
      return True
    elif self.ladoA == self.ladoC and self.ladoA != self.ladoB:
      return True
    elif self.ladoB == self.ladoC and self.ladoB != self.ladoA:
      return True

  def escaleno(self):
    if self.ladoA != self.ladoB and self.ladoA != self.ladoC and self.ladoB != self.ladoC:
      return True


ladoA1 = float(input("Digite o primeiro lado do triângulo: "))
ladoB1 = float(input("Digite o segundo lado do triângulo: "))
ladoC1 = float(input("Digite o terceiro lado do triângulo: "))
tri1 = Triangulo(ladoA1,ladoB1,ladoC1)
print("\n")
print(f'O perímetro do triângulo é: {tri1.calcularPerimetro()}')
print(f'O maior lado do triângulo é: {tri1.getMaiorLado()}')
print("\n")
print(f'O triângulo é Equilátero? {tri1.equilatero()}')
print(f'O triângulo é Isósceles? {tri1.isosceles()}')
print(f'O triângulo é Escaleno? {tri1.escaleno()}')