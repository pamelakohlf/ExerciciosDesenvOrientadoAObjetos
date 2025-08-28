class Passagem:
  def __init__(self,preco,assento):
    self.preco = preco
    self.assento = assento

  def set_alterar_preco(self,novo_preco):
    self.preco = novo_preco
    print(f'O novo preço é: {self.preco}')

  def escolher_assento(self,novo_assento):
    self.assento = novo_assento
    print(f'O novo assento é: {self.assento}')

class PassagemBus(Passagem):
  def __init__(self,preco,assento,placa,leito):
    super().__init__(preco,assento)
    self.placa = placa
    self.leito = leito

  def abastecer(self):
    print("O onibus está abastecendo")

class PassagemAviao(Passagem):
    def __init__(self,preco,assento,portaodeembarque,checkin):
      super().__init__(preco,assento)
      self.portaodeembarque = portaodeembarque
      self.checkin = checkin

    def decolar(self):
      print('O avião está decolando')


p1b = PassagemBus(200,None,"ABC123","Semi-leito")
p1b.abastecer()
print(f'Passagem de onibus valor: R$ {p1b.preco} | assento: {p1b.assento} | placa: {p1b.placa} | leito: {p1b.leito}')
p1b.set_alterar_preco(180)
p1b.escolher_assento(15)
print(f'Passagem de onibus valor: R$ {p1b.preco} | assento: {p1b.assento} | placa: {p1b.placa} | leito: {p1b.leito}')
print("\n")
p1a = PassagemAviao(800,10,150,"Realizado")
print(f'Passagem de avião valor: R$ {p1a.preco} | assento: {p1a.assento} | portaodeembarque: {p1a.portaodeembarque} | check-in: {p1a.checkin}')
p1a.decolar()
