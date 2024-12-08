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
    print("(1) Cadastro de Eventos")
    print("(2) Atualizar Eventos")
    print("(3) Visualizar Eventos")
    print("(4) Excluir Eventos")
    print("(5) Voltar ao Menu Principal \n")

# Função para cadastrar novos eventos
def Cadastrar_Eventos(nome_evento, data_evento, descricao_evento, numero_participantes):
    nome_evento = nome_evento.lower()  # Convertendo o nome do evento para minúsculas
    # Adicionando o evento ao dicionário
    evento[nome_evento] = {"Nome Evento": nome_evento, "Data Evento": data_evento, "Descrição Evento": descricao_evento, "Numero Participantes": numero_participantes, "Inscritos": 0}
    print(f"Evento {nome_evento} cadastrado com sucesso!! \n")

# Função para exibir todos os eventos cadastrados
def exibir_evento():
    if not evento:  # Verificando se o dicionário de eventos está vazio
        print("Sem Evento cadastrado")
    else:
        print("Eventos Cadastrados:")
        # Enumerando e iterando sobre o dicionário de eventos
        for i, (nome_evento, detalhes) in enumerate(evento.items(), start=1):
            vagas_restantes = detalhes["Numero Participantes"] - detalhes["Inscritos"]
            print(f"{i}. Evento: {nome_evento.title()}, Data Evento: {detalhes['Data Evento']}, Descrição Evento: {detalhes['Descrição Evento']}, Numero Participantes: {detalhes['Numero Participantes']}, Vagas Restantes: {vagas_restantes}")
        print()

# Função para obter o nome do evento pelo índice
def obter_evento_por_indice(indice):
    if 0 <= indice < len(evento):
        return list(evento.keys())[indice]
    return None

# Função para inscrever um aluno no evento
def inscrever_aluno(nome_evento, nome_aluno):
    if nome_evento in inscricoes:
        inscricoes[nome_evento].append(nome_aluno)
    else:
        inscricoes[nome_evento] = [nome_aluno]
    evento[nome_evento]["Inscritos"] += 1

# Loop principal do programa
while True:
    print("________Bem-vindo ao Gerenciador de Eventos Universitarios________ \n")
    print("(1) Coordenador")
    print("(2) Aluno \n")

    while True:
        try:
            escolha_perfil = int(input("Você é: "))  # Solicitando a escolha do perfil (Coordenador ou Aluno)
            if escolha_perfil in [1, 2]:
                break
            else:
                print("Escolha inválida. Por favor, insira 1 para Coordenador ou 2 para Aluno.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")  # Tratando entradas inválidas

    if escolha_perfil == 1:
        while True:
            exibir_menu_coordenador()

            try:
                escolha_opcao = int(input("Qual opção você deseja? "))
                if escolha_opcao in [1, 2, 3, 4, 5]:
                    break
                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")

        # Condição para cadastrar novos eventos
        if escolha_opcao == 1:
            nome_evento = input("Digite o nome do Evento: ")
            data_evento = input("Digite data do Evento: ")
            descricao_evento = input("Digite a descrição do evento: ")
            numero_participantes = int(input("Digite o numero de participantes: "))
            Cadastrar_Eventos(nome_evento, data_evento, descricao_evento, numero_participantes)

        # Condição para atualizar eventos existentes
        elif escolha_opcao == 2:
            if not evento:  # Verificação se há eventos disponíveis
                print("Sem eventos disponíveis para atualização.")
                input("Pressione Enter para voltar ao menu principal...")
            else:
                exibir_evento()
                try:
                    indice_evento = int(input("Digite o número do evento que deseja atualizar: ")) - 1
                    nome_evento = obter_evento_por_indice(indice_evento)
                    if nome_evento:
                        data_evento = input("Digite nova data do Evento: ")
                        numero_participantes = int(input("Digite o novo número de participantes: "))
                        evento[nome_evento]["Data Evento"] = data_evento
                        evento[nome_evento]["Numero Participantes"] = numero_participantes
                        print(f"Evento {nome_evento} atualizado com sucesso! \n")
                    else:
                        print("Evento não encontrado. \n")
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número válido.")
                input("Pressione Enter para voltar ao menu principal...")

        # Condição para visualizar eventos cadastrados
        elif escolha_opcao == 3:
            exibir_evento()
            input("Pressione Enter para voltar ao menu principal...")

        # Condição para excluir eventos existentes
        elif escolha_opcao == 4:
            if not evento:  # Verificação se há eventos disponíveis
                print("Sem eventos disponíveis para exclusão.")
                input("Pressione Enter para voltar ao menu principal...")
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
                input("Pressione Enter para voltar ao menu principal...")

        # Condição para voltar ao menu inicial
        elif escolha_opcao == 5:
            continue

    elif escolha_perfil == 2:
        while True:
            exibir_menu_aluno()

            try:
                escolha_opcao = int(input("Qual opção você deseja? "))
                if escolha_opcao in [1, 2, 3]:
                    break
                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")

        # Condição para visualizar eventos cadastrados
        if escolha_opcao == 1:
            exibir_evento()
            input("Pressione Enter para voltar ao menu principal...")

        # Condição para inscrever aluno em evento
        elif escolha_opcao == 2:
            exibir_evento()
            if evento:
                try:
                    indice_evento = int(input("Digite o número do evento em que deseja se inscrever: ")) - 1
                    nome_evento = obter_evento_por_indice(indice_evento)
                    if nome_evento:
                        nome_aluno = input("Digite o nome do aluno: ")
                        if evento[nome_evento]["Inscritos"] < evento[nome_evento]["Numero Participantes"]:
                            inscrever_aluno(nome_evento, nome_aluno)
                            print(f"Aluno {nome_aluno} inscrito com sucesso no evento {nome_evento}! \n")
                        else:
                            print("Não há vagas disponíveis para este evento.\n")
                    else:
                        print("Evento não encontrado. \n")
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número válido.")
            else:
                print("Sem eventos disponíveis para inscrição. \n")
                input("Pressione Enter para voltar ao menu principal...")

        # Condição para voltar ao menu inicial
        elif escolha_opcao == 3:
            continue
