class Imovel:
    def __init__(self, inscricao, aluguel, iptu):
        self.inscricao = inscricao
        self.aluguel = aluguel
        self.iptu = iptu

    def parcela_iptu(self, parcelas=1):
        if parcelas <= 0:
            return "Número inválido de parcelas."
        return self.iptu / parcelas

    def mudar_aluguel(self, novo_aluguel):
        self.aluguel = novo_aluguel
        print(f'Aluguel do imóvel {self.inscricao} mudou para R$ {self.aluguel:.2f}')

class Casa(Imovel):
    def __init__(self, inscricao, aluguel, iptu, quartos, sala, piscina=False):
        super().__init__(inscricao, aluguel, iptu)
        self.quartos = quartos
        self.sala = sala
        self.piscina = piscina

    def mostrar_casa(self):
        info = (f"Casa com {self.quartos} quartos e sala.")
        if self.piscina:
            info += "Tem piscina."
        print(f"Detalhes da Casa {self.inscricao}: {info}")

class Apartamento(Imovel):
    def __init__(self, inscricao, aluguel, iptu, quartos, sala, elevador=False):
        super().__init__(inscricao, aluguel, iptu)
        self.quartos = quartos
        self.sala = sala
        self.elevador = elevador

    def mostrar_apto(self):
        info = (f"Apartamento com {self.quartos} quartos e sala.")
        if self.elevador:
            info += "Tem elevador."
        print(f"Detalhes do Apartamento {self.inscricao}: {info}")

class Terreno(Imovel):
    def __init__(self, inscricao, aluguel, iptu, area):
        super().__init__(inscricao, aluguel, iptu)
        self.area = area

    def mostrar_terreno(self):
        print(f"Terreno {self.inscricao} com {self.area} m².")

class Chacara(Imovel):
    def __init__(self, inscricao, aluguel, iptu, quartos, piscina=False, churrasqueira=False):
        super().__init__(inscricao, aluguel, iptu)
        self.quartos = quartos
        self.piscina = piscina
        self.churrasqueira = churrasqueira

    def mostrar_chacara(self):
        info = (f"Chácara com {self.quartos} quartos.")
        if self.piscina:
            info += "Tem piscina."
        if self.churrasqueira:
            info += "Tem churrasqueira."
        print(f"Detalhes da Chácara {self.inscricao}: {info}")


casa1 = Casa("CASA1", 1200, 150, 3, "grande", True)
casa1.mudar_aluguel(1250)
print(f"IPTU da casa em 2 vezes: R$ {casa1.parcela_iptu(2):.2f}")
casa1.mostrar_casa()

apto1 = Apartamento("APTO1", 850, 90, 2, "pequena", True)
apto1.mostrar_apto()

terreno1 = Terreno("TER1", 300, 40, 500)
terreno1.mostrar_terreno()

chacara1 = Chacara("CHAC1", 1500, 200, 4, True, True)
chacara1.mostrar_chacara()