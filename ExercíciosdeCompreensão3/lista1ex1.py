class Pessoa:
  def __init__(self,nome,idade,endereco):
    self.nome = nome
    self.idade = idade
    self.endereco = endereco

  def get_Nome(self):
    return self.nome

  def set_Idade(self,nova_idade):
    if nova_idade == self.idade:
      print("mesma idade")
    else:
      self.idade = nova_idade

  def imprime_Endereco(self):
    print(self.endereco)

p1 = Pessoa("Joao",20,"R Brasil, 1010")
print(p1.idade)
p1.set_Idade(20)
print(p1.get_Nome())
print(p1.idade)
p1.imprime_Endereco()