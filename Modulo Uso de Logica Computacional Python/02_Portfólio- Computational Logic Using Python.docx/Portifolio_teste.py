# Dicionário para armazenar eventos e inscrições
evento = {}
inscricoes = {}

# Função para exibir o menu do aluno
def exibir_menu_aluno():
    print("________Gerenciar Eventos Universitarios - Aluno________ \n")
    print("(1) Visualizar Eventos")
    print("(2) Inscrever no Evento")
    print("(3) Voltar ao Menu Principal \n")

# Função para exibir o menu do coordenador
def exibir_menu_coordenador():
    print("________Gerenciar Eventos Universitarios - Coordenador________ \n")
    print("(1) Criar Novo Evento")
    print("(2) Atualizar Eventos")
    print("(3) Visualizar Eventos")
    print("(4) Visualizar Inscritos")
    print("(5) Cancelar Evento")
    print("(6) Excluir Eventos")
    print("(7) Voltar ao Menu Principal \n")

# Função para cadastrar novos eventos
def cadastrar_eventos():
    nome_evento = input("Digite o nome do Evento: ").lower()
    data_evento = input("Digite a data do Evento: ")
    descricao_evento = input("Digite a descrição do evento: ")
    numero_participantes = int(input("Digite o número de participantes: "))
    evento[nome_evento] = {
        "Nome Evento": nome_evento,
        "Data Evento": data_evento,
        "Descrição Evento": descricao_evento,
        "Numero Participantes": numero_participantes,
        "Inscritos": 0
    }
    print(f"Evento {nome_evento} cadastrado com sucesso!! \n")

# Função para exibir todos os eventos cadastrados
def exibir_evento():
    if not evento:
        print("Sem Evento cadastrado")
    else:
        print("Eventos Cadastrados:")
        for i, (nome_evento, detalhes) in enumerate(evento.items(), start=1):
            vagas_restantes = detalhes["Numero Participantes"] - detalhes["Inscritos"]
            print(f"{i}. Evento: {nome_evento.title()}, Data: {detalhes['Data Evento']}, Descrição: {detalhes['Descrição Evento']}, Participantes: {detalhes['Numero Participantes']}, Vagas Restantes: {vagas_restantes}")
        print()

# Função para obter o nome do evento pelo índice
def obter_evento_por_indice(indice):
    if 0 <= indice < len(evento):
        return list(evento.keys())[indice]
    return None

# Função para inscrever um aluno no evento
def inscrever_aluno():
    exibir_evento()
    if evento:
        try:
            indice_evento = int(input("Digite o número do evento em que deseja se inscrever: ")) - 1
            nome_evento = obter_evento_por_indice(indice_evento)
            if nome_evento:
                nome_aluno = input("Digite o nome do aluno: ")
                if evento[nome_evento]["Inscritos"] < evento[nome_evento]["Numero Participantes"]:
                    if nome_evento in inscricoes:
                        inscricoes[nome_evento].append(nome_aluno)
                    else:
                        inscricoes[nome_evento] = [nome_aluno]
                    evento[nome_evento]["Inscritos"] += 1
                    print(f"Aluno {nome_aluno} inscrito com sucesso no evento {nome_evento}!\n")
                else:
                    print("Não há vagas disponíveis para este evento.\n")
            else:
                print("Evento não encontrado. \n")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

# Função para exibir inscritos em um evento
def exibir_inscritos():
    exibir_evento()
    try:
        indice_evento = int(input("Digite o número do evento para visualizar os inscritos: ")) - 1
        nome_evento = obter_evento_por_indice(indice_evento)
        if nome_evento:
            if nome_evento in inscricoes and inscricoes[nome_evento]:
                print(f"Inscritos no evento {nome_evento.title()}:")
                for nome_aluno in inscricoes[nome_evento]:
                    print(f"- {nome_aluno}")
            else:
                print(f"Sem inscritos no evento {nome_evento.title()}.\n")
        else:
            print("Evento não encontrado. \n")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")

# Função para cancelar eventos existentes
def cancelar_eventos():
    if not evento:
        print("Sem eventos disponíveis para cancelamento.")
    else:
        exibir_evento()
        try:
            indice_evento = int(input("Digite o número do evento que deseja cancelar: ")) - 1
            nome_evento = obter_evento_por_indice(indice_evento)
            if nome_evento:
                confirmacao = input(f"Tem certeza que deseja cancelar o evento {nome_evento.title()}? (s/n): ").lower()
                if confirmacao == 's':
                    del evento[nome_evento]
                    if nome_evento in inscricoes:
                        del inscricoes[nome_evento]
                    print(f"Evento {nome_evento} cancelado com sucesso! \n")
                else:
                    print("Cancelamento de evento cancelado. \n")
            else:
                print("Evento não encontrado. \n")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

# Função para excluir eventos existentes
def excluir_eventos():
    if not evento:
        print("Sem eventos disponíveis para exclusão.")
        input("Pressione Enter para voltar ao menu dos coordenadores...")
    else:
        exibir_evento()
        try:
            indice_evento = int(input("Digite o número do evento que deseja excluir: ")) - 1
            nome_evento = obter_evento_por_indice(indice_evento)
            if nome_evento:
                confirmacao = input(f"Tem certeza que deseja excluir o evento {nome_evento.title()}? (s/n): ").lower()
                if confirmacao == 's':
                    del evento[nome_evento]
                    print(f"Evento {nome_evento} excluído com sucesso! \n")
                else:
                    print("Exclusão de evento cancelada. \n")
            else:
                print("Evento não encontrado. \n")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")
        input("Pressione Enter para voltar ao menu dos coordenadores...")

# Loop principal do programa
while True:
    print("________Bem-vindo ao Gerenciador de Eventos UniFECAF________ \n")
    print("(1) Coordenador")
    print("(2) Aluno \n")

    while True:
        try:
            escolha_perfil = int(input("Você é: "))
            if escolha_perfil in [1, 2]:
                break
            else:
                print("Escolha inválida. Por favor, insira 1 para Coordenador ou 2 para Aluno.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

    if escolha_perfil == 1:
        while True:
            exibir_menu_coordenador()
            try:
                escolha_opcao = int(input("Qual opção você deseja? "))
                if escolha_opcao == 1:
                    cadastrar_eventos()
                elif escolha_opcao == 2:
                    atualizar_eventos()
                elif escolha_opcao == 3:
                    exibir_evento()
                    input("Pressione Enter para voltar ao menu dos coordenadores...")
                elif escolha_opcao == 4:
                    exibir_inscritos()
                    input("Pressione Enter para voltar ao menu dos coordenadores...")
                elif escolha_opcao == 5:
                    cancelar_eventos()
                    input("Pressione Enter para voltar ao menu dos coordenadores...")
                elif escolha_opcao == 6:
                    excluir_eventos()
                    input("Pressione Enter para voltar ao menu dos coordenadores...")
                elif escolha_opcao == 7:
                    break
                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")

    elif escolha_perfil == 2:
        while True:
            exibir_menu_aluno()
            try:
                escolha_opcao = int(input("Qual opção você deseja? "))
                if escolha_opcao == 1:
                    exibir_evento()
                    input("Pressione Enter para voltar ao menu do aluno...")
                elif escolha_opcao == 2:
                    inscrever_aluno()
                    input("Pressione Enter para voltar ao menu do aluno...")
                elif escolha_opcao == 3:
                    break
                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")
