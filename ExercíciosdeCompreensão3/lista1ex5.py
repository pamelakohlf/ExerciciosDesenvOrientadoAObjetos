# O enunciado dessa 5 está muito confuso, fiz o que entendi dele.
class Funcionario:
  def __init__(self,nome,sobrenome,horas_trabalhadas,valor_hora):
    self.nome = nome
    self.sobrenome = sobrenome
    self.horas_trabalhadas = horas_trabalhadas
    self.valor_hora = valor_hora

  def nomeCompleto(self):
    print(f'Nome completo do funcionario: {self.nome} {self.sobrenome}')

  def calcularSalario(self):
    salario = self.horas_trabalhadas * self.valor_hora
    print(f'O salário é: R$ {salario}')

  def set_incrementarHoras(self,add_valor):
    novo_valor = self.valor_hora + add_valor
    self.valor_hora = novo_valor
    print(f'Novo valor por hora é: R$ {self.valor_hora}')


func1 = Funcionario("Ana","Silva",240,10)
func1.nomeCompleto()
func1.calcularSalario()
func1.set_incrementarHoras(10)
func1.calcularSalario()