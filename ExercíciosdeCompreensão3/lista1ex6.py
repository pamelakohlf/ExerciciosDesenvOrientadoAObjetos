class Circulo:
  def __init__(self,raio):
    self.raio = raio

  def imprimeValor(self):
    print(f'O valor do raio é: {self.raio}')

  def area(self):
    area = (self.raio**2) * 3.14159
    print(f'A área do circulo é: {area}')

  def circunf(self):
    circunf = 2 * 3.14159 * self.raio
    print(f'A circunferência do circulo é: {circunf}')


cir1 = Circulo(5)
cir1.imprimeValor()
cir1.area()
cir1.circunf()