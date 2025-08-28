class Pessoa:
  def __init__(self,matricula,nome,idade):
    self.matricula = matricula
    self.nome = nome
    self.idade = idade

class Aluno(Pessoa):
  def __init__(self,matricula,nome,idade,notas=None,media=0):
    super().__init__(matricula,nome,idade)
    if notas is None:
      self.notas = []
    else:
      self.notas = notas
    self.media = media

  def set_calcular_media(self):
    if self.notas:
      self.media = sum(self.notas) / len(self.notas)
      print(f'A média é: {self.media:.2f}')
    else:
      print('O aluno não possui notas para calcular a média.')
      self.media = 0


class Professor(Pessoa):
  def __init__(self,matricula,nome,idade,formacao,disciplina,cargah,salario):
    super().__init__(matricula,nome,idade)
    self.formacao = formacao
    self.disciplina = disciplina
    self.cargah = cargah
    self.salario = salario

  def lecionar(self):
    print("O prof está dando aula")

a1 = Aluno(1212,"Julia",16,[10,9,10])
a1.set_calcular_media()

p1 = Professor(1111,"Tiago",35,"ADS","Objetos",120,5000)
p1.lecionar()