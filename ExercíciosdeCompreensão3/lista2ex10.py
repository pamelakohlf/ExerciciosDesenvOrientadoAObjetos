class Cliente:
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco

    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf

    def get_endereco(self):
        return self.endereco

    def set_endereco(self, endereco):
        self.endereco = endereco

class ContaBancaria:
    def __init__(self, numero_conta, titular):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = 0.0

    def get_numero_conta(self):
        return self.numero_conta

    def get_titular(self):
        return self.titular

    def get_saldo(self):
        return self.saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado na conta {self.numero_conta}.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado na conta {self.numero_conta}.")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

class ContaCorrente(ContaBancaria):
    def __init__(self, numero_conta, titular, limite=1000.0):
        super().__init__(numero_conta, titular)
        self.limite = limite

    def get_limite(self):
        return self.limite

    def set_limite(self, limite):
        self.limite = limite

    def sacar(self, valor):
        if valor > 0 and (self.saldo + self.limite) >= valor:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado na conta corrente {self.numero_conta}.")
        else:
            print("Saldo insuficiente ou limite excedido para saque.")

class ContaPoupanca(ContaBancaria):
    def __init__(self, numero_conta, titular, taxa_juros=0.01):
        super().__init__(numero_conta, titular)
        self.taxa_juros = taxa_juros

    def get_taxa_juros(self):
        return self.taxa_juros

    def set_taxa_juros(self, taxa_juros):
        self.taxa_juros = taxa_juros

    def aplicar_juros(self):
        juros = self.saldo * self.taxa_juros
        self.saldo += juros
        print(f"Juros de R$ {juros:.2f} aplicados na conta poupança {self.numero_conta}.")

class AplicacaoFundo(ContaBancaria):
    def __init__(self, numero_conta, titular, nome_fundo, taxa_rendimento=0.02):
        super().__init__(numero_conta, titular)
        self.nome_fundo = nome_fundo
        self.taxa_rendimento = taxa_rendimento

    def get_nome_fundo(self):
        return self.nome_fundo

    def get_taxa_rendimento(self):
        return self.taxa_rendimento

    def set_taxa_rendimento(self, taxa_rendimento):
        self.taxa_rendimento = taxa_rendimento

    def calcular_rendimento(self):
        rendimento = self.saldo * self.taxa_rendimento
        print(f"O rendimento da aplicação {self.nome_fundo} na conta {self.numero_conta} é de R$ {rendimento:.2f}.")
        return rendimento


cliente1 = Cliente("Ana Silva", "123.456.789-00", "Rua das Flores, 123")
conta_corrente1 = ContaCorrente("CC001", cliente1)
conta_poupanca1 = ContaPoupanca("CP002", cliente1, 0.015)
aplicacao1 = AplicacaoFundo("AF003", cliente1, "Fundo DI", 0.025)

print(f"Titular da CC001: {conta_corrente1.get_titular().get_nome()}")
conta_corrente1.depositar(500.00)
conta_corrente1.sacar(200.00)
conta_corrente1.sacar(1500.00) 
print(f"Saldo CC001: R$ {conta_corrente1.get_saldo():.2f}")

conta_poupanca1.depositar(1000.00)
conta_poupanca1.aplicar_juros()
print(f"Saldo CP002: R$ {conta_poupanca1.get_saldo():.2f}")

aplicacao1.depositar(2000.00)
aplicacao1.calcular_rendimento()
print(f"Saldo AF003: R$ {aplicacao1.get_saldo():.2f}")