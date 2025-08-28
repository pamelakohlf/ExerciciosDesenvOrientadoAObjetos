class Evento:
    def __init__(self,nome,valor,data):
        self.nome = nome
        self.valor = valor 
        self.data = data
    
    def __str__(self):
        return f"Evento: {self.nome} | Valor: {self.valor} | Data: {self.data}"
    


def carregar_eventos():
    eventos = []
    try:
        with open('eventos.txt', 'r', encoding='utf-8') as arq:
            for linha in arq:
                try:
                    nome, valor, data = linha.strip().split(",", 2)# Divide a linha em no máximo 3 partes: nome, valor, data
                    eventos.append(Evento(nome, valor, data))
                except ValueError:
                    print(f"Aviso: Linha de evento mal formatada, ignorada: '{linha.strip()}'")
    except FileNotFoundError:
        pass
    return eventos



def salvar_evento(Evento):
    try:
         with open('eventos.txt', 'a', encoding='utf-8') as arq:
            arq.write(f'{Evento.nome},{Evento.valor},{Evento.data}\n')
    
    except Exception as e:
        print(f"Erro ao salvar evento '{Evento.nome}': {e}")


def buscar_evento_por_nome(nome):
    eventos = carregar_eventos()
    for evento in eventos:
        if evento.nome == nome:
            return evento
    return None
