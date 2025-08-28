class Carro:
  def __init__(self,marca,modelo,cor,ano,valor,consumo,nivel=0):
    self.marca = marca
    self.modelo = modelo
    self.cor = cor
    self.ano = ano
    self.valor = valor
    self.consumo = consumo
    self.nivel = nivel
    self.distancia = 0

  def set_abastecer(self,abastecer):
    novo_nivel = self.nivel + abastecer
    self.nivel = novo_nivel
    print(f'O novo nível é: {self.nivel}')

  def andar(self,km):
    self.distancia = km
    print(f'A distancia percorrida foi: {self.distancia}')

  def set_verificar_nivel(self):
    calcula = self.distancia / self.consumo
    novo_nivel = self.nivel - calcula
    self.nivel = novo_nivel
    print(f'Para andar {self.distancia} km, foram gastos {calcula:.2f} e o novo nivel é: {self.nivel:.2f}')


  def calcular_imposto(self):
    calculo = self.valor * 0.035
    print(f'O valor do IPVA é: R$ {calculo:.2f}')

car1 = Carro("fiat","pulse","branco",2024,105000,12)
car1.set_abastecer(10)
car1.set_abastecer(20)
car1.andar(200)
car1.set_verificar_nivel()
car1.calcular_imposto()