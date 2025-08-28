class Brinquedo:
  def __init__(self,nome,cor,tamanho,preco):
    self.nome = nome
    self.cor = cor
    self.tamanho = tamanho
    self.preco = preco

  def brincar(self):
    print(f'Estou brincando com o {self.nome}')

class Carrinho(Brinquedo): #1
  def __init__(self,nome,cor,tamanho,preco,tipo):
    super().__init__(nome,cor,tamanho,preco)
    self.tipo = tipo

  def brincar(self):
    print(f'O {self.nome} está em uma corrida')

class VideoGame(Brinquedo): #2
  def __init__(self,nome,cor,tamanho,preco,bateria):
    super().__init__(nome,cor,tamanho,preco)
    self.bateria = bateria

  def brincar(self):
    print(f'O {self.nome} está ligado')

class Aviao(Brinquedo): #3
  def __init__(self,nome,cor,tamanho,preco,peso):
    super().__init__(nome,cor,tamanho,preco)
    self.peso = peso

  def brincar(self):
    print(f'O {self.nome} está voando')


class Nave(Brinquedo): #4
  def __init__(self,nome,cor,tamanho,preco,planeta):
    super().__init__(nome,cor,tamanho,preco)
    self.planeta = planeta

  def brincar(self):
    print(f'O {self.nome} está no planeta {self.planeta}')


class Guerreiro(Brinquedo): #5
  def __init__(self,nome,cor,tamanho,preco,luta):
    super().__init__(nome,cor,tamanho,preco)
    self.luta = luta

  def brincar(self):
    print(f'O {self.nome} está lutando')

b1 = Carrinho("Relampago","preto","pequeno",80,"de corrida")
b1.brincar()

b2 = VideoGame("Play1","preto","medio",500,"energia")
b2.brincar()

b3 = Aviao("Azul","branco","pequeno",200,100)
b3.brincar()

b4 = Nave("JUNP","amarela","pequena",300,"Marte")
b4.brincar()

b5 = Guerreiro("XX2","branco","pequeno",50,"Karate")
b5.brincar()