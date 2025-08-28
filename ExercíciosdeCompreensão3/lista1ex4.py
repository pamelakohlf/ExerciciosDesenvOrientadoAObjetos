class Conta:
  def __init__(self,nome,cpf,numero,saldo):
    self.nome = nome
    self.cpf = cpf
    self.numero = numero
    self.saldo = saldo

  def set_depositar(self,deposito,novo_saldo=0):
    novo_saldo = self.saldo + deposito
    self.saldo = novo_saldo
    print(f'Deposito de: R$ {deposito} realizado | Novo saldo = R$ {novo_saldo}')

  def set_sacar(self,sacado):
    if sacado > self.saldo:
      print("Saldo insuficiente")
    else:
      novo_saldo = self.saldo - sacado
      self.saldo = novo_saldo
      print(f'Saque de: R$ {sacado} realizado | Novo saldo = R$ {novo_saldo}')

  def imprimir_saldo(self):
    print(f'Saldo da conta: R$ {self.saldo}')

c1 = Conta("Carol","05616456",123,100)
c1.imprimir_saldo()

c1.set_depositar(200)
c1.set_sacar(500)
c1.set_sacar(300)
c1.imprimir_saldo()