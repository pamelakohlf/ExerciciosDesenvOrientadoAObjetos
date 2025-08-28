# usuario.py

class Usuario:
    def __init__(self, nome, email, telefone, eventos_inscritos=None):
        self.nome = nome
        self.__email = email
        self.__telefone = telefone
        self.eventos_inscritos = eventos_inscritos if eventos_inscritos is not None else []
    def get_email(self):
        return self.__email

    def get_telefone(self):
        return self.__telefone

    def set_email(self, email):
        if "@" in email and "." in email.split("@")[1]:
            self.__email = email
        else:
            print("Aviso: E-mail inválido. Por favor, verifique o formato.")

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def __str__(self):
        eventos_str = "; ".join(self.eventos_inscritos) if self.eventos_inscritos else "Nenhum"
        return f"Usuário: {self.nome} | E-mail: {self.__email} | Telefone: {self.__telefone} | Eventos: {eventos_str}"

    def adicionar_evento(self, nome_evento):
        if nome_evento not in self.eventos_inscritos:
            self.eventos_inscritos.append(nome_evento)
            print(f"'{nome_evento}' adicionado aos eventos de {self.nome}.")
        else:
            print(f"'{nome_evento}' já está nos eventos de {self.nome}.")

    def listar_eventos_inscritos(self):
        if not self.eventos_inscritos:
            return "Nenhum evento inscrito."
        return ", ".join(self.eventos_inscritos)

def carregar_usuarios():
    usuarios = []
    try:
        with open('usuarios.txt', 'r', encoding='utf-8') as arq:
            for linha in arq:
                try:
                    partes = linha.strip().split(",", 3)
                    nome, email, telefone = partes[0], partes[1], partes[2]
                    eventos_str = partes[3] if len(partes) > 3 else ""
                    eventos_inscritos = eventos_str.split(";") if eventos_str else []
                    usuarios.append(Usuario(nome, email, telefone, eventos_inscritos))
                except ValueError:
                    print(f"Aviso: Linha de usuário mal formatada, ignorada: '{linha.strip()}'")
    except FileNotFoundError:
        pass 
    return usuarios

def salvar_usuario(usuario_para_salvar):
    todos_usuarios_atuais = carregar_usuarios()
    usuarios_sem_duplicata = [u for u in todos_usuarios_atuais if u.get_email() != usuario_para_salvar.get_email()]
    usuarios_sem_duplicata.append(usuario_para_salvar)

    try:
        with open('usuarios.txt', 'w', encoding='utf-8') as arq: 
            for u in usuarios_sem_duplicata:
                eventos_str = ";".join(u.eventos_inscritos) 
                arq.write(f"{u.nome},{u.get_email()},{u.get_telefone()},{eventos_str}\n")
    except Exception as e:
        print(f"Erro ao salvar/atualizar usuário '{usuario_para_salvar.nome}': {e}")

def buscar_usuario_por_email(email):
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario.get_email() == email:
            return usuario
    return None
