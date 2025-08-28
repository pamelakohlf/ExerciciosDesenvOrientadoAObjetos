class Ingresso:
  def __init__(self,preco,setor):
    self.preco = preco
    self.setor = setor

  def set_alterar_preco(self,novo_preco):
    self.preco = novo_preco
    print(f'O novo preço é: {self.preco}')

  def mostrar_setor(self):
    print(f'O setor é: {self.setor}')

class IngressoVIP(Ingresso):
  def __init__(self,preco,setor,camarote=False,open_bar=False,open_food=False,estacionamento=False):
    super().__init__(preco,setor)
    self.camarote = camarote
    self.open_bar = open_bar
    self.open_food = open_food
    self.estacionamento = estacionamento

  def pegar_bebida(self):
    if self.open_bar:
      print('Liberado a pegar bebida')
    else:
      print("Sem open bar, bloqueado")


  def acessar_camarote(self):
    if self.camarote:
      print("Ingresso com acesso ao camarote")
    else:
      print("Ingresso sem acesso ao camarote")

ing1 = IngressoVIP(200,"A",camarote=True, open_bar=True, open_food=True, estacionamento=True)
print(ing1.preco)
ing1.set_alterar_preco(250)
ing1.pegar_bebida()
ing1.acessar_camarote()

ing2 = IngressoVIP(200,"C",camarote=False, open_bar=False, open_food=False, estacionamento=True)
ing2.pegar_bebida()
ing2.acessar_camarote()
ing2.mostrar_setor()