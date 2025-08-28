class Aluno_Academia:
  def __init__(self,nome,idade,peso,altura,mensalidade=120.00):
    self.nome = nome
    self.idade = idade
    self.peso = peso
    self.altura = altura
    self.mensalidade = mensalidade

  def Calcular_IMC(self):
    imc = self.peso / (self.altura ** 2)
    print(f'O IMC do aluno é: {imc}')

  def Obter_valor_mensalidade(self,mensalidade_menor=0):
    if self.idade < 18:
      mensalidade_menor = self.mensalidade * 0.5
      print(f'O valor da mensalidade é: R$ {mensalidade_menor}')
    else:
      print(f'O valor da mensalidade é: R$ {self.mensalidade}')

aluno1 = Aluno_Academia("Joana",20,60,1.65)
aluno1.Calcular_IMC()
aluno1.Obter_valor_mensalidade()

print("\n")

aluno2 = Aluno_Academia("Camila",16,65,1.72)
aluno2.Calcular_IMC()
aluno2.Obter_valor_mensalidade()