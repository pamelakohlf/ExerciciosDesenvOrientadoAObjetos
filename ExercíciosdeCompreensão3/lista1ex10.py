class NF:
  def __init__(self, numero,tipo,serie,cnpj,razao,data,icms,frete,ipi,valor):
    self.numero = numero
    self.tipo = tipo
    self.serie = serie
    self.cnpj = cnpj
    self.razao = razao
    self.data = data
    self.icms = icms
    self.frete = frete
    self.ipi = ipi
    self.valor = valor

  def obterNumero(self):
    return self.numero

  def obterDataEmissao(self):
    return self.data

  def set_alterarRazaoSocial(self,nova_razao):
    self.razao = nova_razao
    print(f"Razão social alterada para {self.razao}")

  def calcularValorTotal(self):
    valor_total = self.valor + self.frete + self.icms + self.ipi
    print(f'O valor total da nota é: R$ {valor_total:.2f}')


nf1 = NF(123,"Entrada","1","123456/0001-00","ABC LTDA","10/01/2025",20,100,10,1000)
print(nf1.razao)
print(nf1.obterNumero())
print(nf1.obterDataEmissao())
nf1.set_alterarRazaoSocial("ABC S.A")
nf1.calcularValorTotal()