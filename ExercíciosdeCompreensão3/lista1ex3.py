class Aluno:
  def __init__(self,nome,ra,n1,n2,n3,n4,media=0):
    self.nome = nome
    self.ra = ra
    self.n1 = n1
    self.n2 = n2
    self.n3 = n3
    self.n4 = n4
    self.media = (n1+n2+n3+n4)/4

  def mostrar_situacao(self):
    if self.media >= 7:
      mostrar_situacao = "Aprovado"
      return mostrar_situacao
    elif self.media >=5 and self.media < 7:
      mostrar_situacao = "Exame"
      return mostrar_situacao
    else:
      mostrar_situacao = "Reprovado"
      return mostrar_situacao


aluno1 = Aluno("Maria",123,10,9,8,7)
print(f'Aluno: {aluno1.nome} | RA: {aluno1.ra} | Situação: {aluno1.mostrar_situacao()}')

aluno2 = Aluno("José",124,7,6,5,4)
print(f'Aluno: {aluno2.nome} | RA: {aluno2.ra} | Situação: {aluno2.mostrar_situacao()}')

aluno3 = Aluno("Carol",125,5,4,3,2)
print(f'Aluno: {aluno3.nome} | RA: {aluno3.ra} | Situação: {aluno3.mostrar_situacao()}')