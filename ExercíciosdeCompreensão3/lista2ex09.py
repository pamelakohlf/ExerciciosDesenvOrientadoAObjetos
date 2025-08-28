class Compra:
    def __init__(self, numero, produto, valor):
        self.numero = numero
        self.produto = produto
        self.valor = valor
        self.valor_total = 0

    def calcular_valor_total(self):
        icms = self.valor * 0.17
        frete = self.valor * 0.05
        self.valor_total = self.valor + icms + frete
        return self.valor_total

class CompraAvista(Compra):
    def __init__(self, numero, produto, valor):
        super().__init__(numero, produto, valor)
        self.desconto = 0

    def calcular_valor_total(self, desconto):
        icms = self.valor * 0.17
        frete = self.valor * 0.05
        self.desconto = desconto
        self.valor_total = self.valor + icms + frete - desconto
        return self.valor_total

    def get_desconto(self):
        return self.desconto

    def set_desconto(self, novo_desconto):
        self.desconto = novo_desconto
        self.calcular_valor_total(self.desconto)

class CompraParcelada(Compra):
    def __init__(self, numero, produto, valor, numero_parcelas=1):
        super().__init__(numero, produto, valor)
        self.numero_parcelas = numero_parcelas

    def simular_numero_de_parcelas(self, parcelas_desejadas):
        valor_parcela = self.calcular_valor_total() / parcelas_desejadas
        print(f'O valor total de R$ {self.valor_total:.2f} em {parcelas_desejadas} parcelas seria de R$ {valor_parcela:.2f} por parcela.')

    def get_numero_parcelas(self):
        return self.numero_parcelas

    def set_numero_parcelas(self, novas_parcelas):
        self.numero_parcelas = novas_parcelas

compra1 = Compra(1, "Televisão", 1000)
valor_final_1 = compra1.calcular_valor_total()
print(f"Compra {compra1.numero} - Produto: {compra1.produto}, Valor Original: R$ {compra1.valor:.2f}, Valor Total: R$ {compra1.valor_total:.2f}")

compra_avista1 = CompraAvista(2, "Smartphone", 800)
valor_final_avista = compra_avista1.calcular_valor_total(50)
print(f"Compra à Vista {compra_avista1.numero} - Produto: {compra_avista1.produto}, Valor Original: R$ {compra_avista1.valor:.2f}, Desconto: R$ {compra_avista1.desconto:.2f}, Valor Total: R$ {compra_avista1.valor_total:.2f}")

compra_parcelada1 = CompraParcelada(3, "Geladeira", 1500, 5)
compra_parcelada1.calcular_valor_total()
print(f"Compra Parcelada {compra_parcelada1.numero} - Produto: {compra_parcelada1.produto}, Valor Original: R$ {compra_parcelada1.valor:.2f}, Valor Total: R$ {compra_parcelada1.valor_total:.2f}, Parcelas: {compra_parcelada1.numero_parcelas}")
compra_parcelada1.simular_numero_de_parcelas(10)