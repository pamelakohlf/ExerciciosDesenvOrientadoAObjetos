class Funcionario:
  def __init__(self,nome, matricula,salario):
    self.nome = nome
    self.matricula = matricula
    self.salario = salario
    self.ponto = []

  def Bater_ponto(self,ponto):
    self.ponto.append(ponto)

class Vendedor(Funcionario):
  def __init__(self,nome, matricula,salario,comissao):
    super().__init__(nome, matricula,salario)
    self.comissao = comissao

  def bater_meta(self,vendas):
    if vendas > 1000:
      print("Bateu a meta")
    else:
      print("Ainda não bateu a meta")

class Gerente(Funcionario):
  def __init__(self,nome, matricula,salario,senha):
    super().__init__(nome, matricula,salario)
    self.senha = senha

  def concluir_projeto(self,projeto_finalizado):
    if projeto_finalizado == "Sim":
      print("Concluiu o projeto")
    elif projeto_finalizado == "Não":
      print("Ainda não concluiu o projeto")

func1 = Vendedor("Marcos", 1010,3000,300)
func1.Bater_ponto(1)
func1.bater_meta(200)
func1.Bater_ponto(1)
print(f'Pontos batidos: {func1.ponto}')
func1.bater_meta(1500)
print("\n")

func2 = Gerente("Luis",2020,5000,123456)
func2.concluir_projeto("Sim")
