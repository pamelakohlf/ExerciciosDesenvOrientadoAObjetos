class Filme:
  def __init__(self,nome,duracao):
    self.nome = nome
    self.duracao = duracao

  def play(self):
    print("O filme foi iniciado")

class Acao(Filme):
  def __init__(self,nome,duracao):
    super().__init__(nome, duracao)

  def explodir(self):
    print("Houve uma explosão")

class Drama(Filme):
  def __init__(self,nome,duracao):
    super().__init__(nome, duracao)

  def discussao(self):
    print("Houve uma discussão")

class Suspense(Filme):
  def __init__(self,nome,duracao):
    super().__init__(nome, duracao)

  def silencio(self):
    print("Houve uma cena silenciosa")

f1 = Filme("A",120)
f1.play()

f2 = Acao("B",100)
print(f'Filme: {f2.nome}')
f2.explodir()

f3 = Drama("C",110)
print(f'Filme: {f3.nome}')
f3.discussao()

f4 = Suspense("D",160)
print(f'Filme: {f4.nome}')
f4.silencio()