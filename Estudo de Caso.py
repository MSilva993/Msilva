# Desenvolvendo um Sistema de Controle de Estoque com Python

# O sistema deve ser capaz de adicionar novos produtos,
# atualizar produtos existentes e visualizar o estoque, além de fornecer funcionalidades
# adicionais

# Implemente um menu de opções para o usuário, permitindo que ele selecione
# diferentes funcionalidades do sistema.

# Inclua as opções de adicionar produto, atualizar produto, excluir produto, 
# visualizar estoque e sair do sistema.

# 1 - Adicionar produto, o sistema deve solicitar as seguintes informações:
# Nome do produto
# Preço do produto
# Quantidade em estoque

# 2 - Atualizar produto: o sistema deve pedir o nome do produto para atualizar e
# solicitar as seguintes informações para atualizar
# Preço do produto
# Quantidade em estoque

# 3 - Excluir produto
# o sistema deve pedir o nome para excluir o produto

# 4 - Visualizar estoque: o sistema deverá mostrar a lista de
# produtos, com as seguinte informações:
# Nome do produto
# Preço do produto
# Quantidade em estoque

# Dicionário para armazenar os produtos
estoque = {}

# Função para exibir o menu
def exibir_menu():
    print("___________Empório dos Eletrônicos___________ \n")
    print("(1) Adicionar produto")
    print("(2) Atualizar produto")
    print("(3) Excluir produto")
    print("(4) Visualizar Estoque")
    print("(5) Sair \n")

# Função para adicionar ou atualizar um produto
def adicionar_ou_atualizar_produto(nome, preco, quantidade):
    nome = nome.lower()  # Converte o nome do produto para minúsculas
    estoque[nome] = {"Preço": preco, "Quantidade": quantidade}
    print(f"Produto {nome} adicionado/atualizado com sucesso! \n")

# Função para exibir o estoque atual
def exibir_estoque():
    if not estoque:
        print("O estoque está vazio.")
    else:
        print("Estoque Atual:")
        for produto, detalhes in estoque.items():
            print(f"Produto: {produto.title()}, Preço: R$ {detalhes['Preço']}, Quantidade: {detalhes['Quantidade']}")
        print()  # Linha em branco para melhor legibilidade

# Loop principal do programa
while True:
    exibir_menu()
    
    # Verificação do input para evitar erros
    while True:
        try:
            escolha_opcao = int(input("Quais das opções você deseja? "))
            break  # Sai do loop se a entrada for um número válido
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
    
    if escolha_opcao == 1:
        nome_produto = input("Digite o nome do produto: ")
        preco = float(input("Digite o valor do produto: "))
        quantidade = int(input("Digite a quantidade desejada: "))
        adicionar_ou_atualizar_produto(nome_produto, preco, quantidade)

    elif escolha_opcao == 2:
        exibir_estoque()  # Exibir o estoque antes de atualizar
        nome_produto = input("Escreva o nome do produto que deseja atualizar: ").lower()  # Converte para minúsculas
        if nome_produto in estoque:
            preco = float(input("Digite o valor do produto: "))
            quantidade = int(input("Digite a quantidade desejada: "))
            adicionar_ou_atualizar_produto(nome_produto, preco, quantidade)
        else:
            print("Produto não existe no estoque\n")

    elif escolha_opcao == 3:
        exibir_estoque()  # Exibir o estoque antes de excluir
        nome_produto = input("Nome do produto que deseja excluir: ").lower()
        if nome_produto in estoque:
            confirmacao = input(f"Gostaria de excluir {nome_produto.title()}? (S/N): ").lower()
            if confirmacao == "s":
                del estoque[nome_produto]
                print(f"Produto {nome_produto.title()} excluído com sucesso!\n")
            else:
                print("Exclusão cancelada. Produto não foi removido.\n")
        else:
            print(f"Produto {nome_produto} não existe\n")

    elif escolha_opcao == 4:
        exibir_estoque()  # Exibir o estoque na opção 4 também
        input("Pressione Enter para voltar ao menu principal...")  # Pausa para o usuário visualizar o estoque

    elif escolha_opcao == 5:
        print("Fim do menu \n")
        break

    else:
        print("Opção inválida\n")
