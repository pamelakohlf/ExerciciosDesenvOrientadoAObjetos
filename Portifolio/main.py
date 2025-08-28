from usuario import *   
from eventos import * 


def inicializar_arquivos():
    try:
        with open('usuarios.txt', 'w', encoding='utf-8')as arq:
            arq.write('')
            print('Arquivo usuarios.txt inicializado')
    except Exception as error:
        print(f'Erro ao inicializar usuarios.txt: {error}')

    try:
        eventos_existentes = carregar_eventos()
        if not eventos_existentes: #Cria eventos caso a lista esteja vazia
            print("Criando 'eventos.txt' com eventos de exemplo...")
            salvar_evento(Evento("Conferencia Python", "Conferencia anual de Python", "2025-07-10"))
            salvar_evento(Evento("Workshop IA", "Introducao a Inteligencia Artificial", "2025-08-05"))
            salvar_evento(Evento("Hackathon Devs", "Maratona de programacao", "2025-09-01"))
            print("Eventos de exemplo adicionados a 'eventos.txt'.")
        else:
            print("Arquivo 'eventos.txt' já contém eventos.")
    except Exception as e:
        print(f"Erro ao inicializar 'eventos.txt': {e}")




def menu_principal():
    while True:
        print("\n--- Plataforma de Cadastro de Eventos ---")
        print("1. Cadastrar novo usuário")
        print("2. Listar eventos disponíveis")
        print("3. Inscrever usuário em evento")
        print("4. Listar eventos de um usuário")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_usuario_interativo()
        elif opcao == '2':
            exibir_eventos_disponiveis()
        elif opcao == '3':
            inscrever_usuario_em_evento()
        elif opcao == '4':
            listar_eventos_do_usuario_interativo()
        elif opcao == '5':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


def cadastrar_usuario_interativo(): #Cadastra o usuario e salva ele
    print("\n--- Cadastro de Novo Usuário ---")
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o e-mail do usuário: ")
    telefone = input("Digite o telefone do usuário: ")

    novo_usuario = Usuario(nome, email, telefone)
    salvar_usuario(novo_usuario)
    print(f"Usuário '{nome}' cadastrado com sucesso!")
    print(novo_usuario)


def exibir_eventos_disponiveis():
    print("\n----Eventos Disponiveis----")
    eventos = carregar_eventos()
    if not eventos:
        print("Nenhum evento disponível no momento")
        return
    
    for i, evento in enumerate(eventos):
        print(f'{i+1}. {evento}')

    

def inscrever_usuario_em_evento():
    print(f"\n---Inscrição em Eventos---")
    email_usuario = input("Digite o email do usuario para realizar a inscrição: ")
    usuario = buscar_usuario_por_email(email_usuario)

    if not usuario:
        print(f"Usuario com email {email_usuario} não encontrado")
        return
    
    while True:
        nome_evento = input("Digite o nome do evento para se inscrever ou sair para finalizar: ")
        if nome_evento.lower() == 'sair':
            break

        evento_existe = buscar_evento_por_nome(nome_evento)
        if not evento_existe:
            print(f"Evento {nome_evento} não encontrado, Verifique a ortografia ")
            continue

        usuario.adicionar_evento(nome_evento)
        salvar_usuario(usuario)
        print(f"Usuário '{usuario.nome}' inscrito no evento '{nome_evento}'.")

def listar_eventos_do_usuario_interativo():
    print("\n--- Meus Eventos ---")
    email_usuario = input("Digite o e-mail do usuário para listar os eventos: ")
    usuario = buscar_usuario_por_email(email_usuario)

    if not usuario:
        print(f"Usuário com e-mail '{email_usuario}' não encontrado.")
        return
    print(f"\nEventos de {usuario.nome}:")
    print(usuario.listar_eventos_inscritos())

if __name__ == "__main__":
    inicializar_arquivos() # Garante que os arquivos existam e tenham eventos iniciais
    menu_principal() 