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

estoque = {}

print("Empório dos Eletrônicos")

while True:
    print("Escolha uma Opção:\n(1) Adicionar produto. \n(2) Atualizar produto. \n(3) Excluir produto \n(4) Visualizar Estoque \n(5) Sair \n")

    Escolha_opcao = int (input("Escolha Opção desejada: "))
    
    if Escolha_opcao == 1:
        Nome_produto = input("Digite nome do Produto: ")
        Preco = float(input("Digite o Valor do Produto: "))
        Quantidade = int(input("Digite a quantidade desejada: "))
        estoque[Nome_produto]= {"Preço": Preco, "Quantidade": Quantidade} 
        print(f"Produto {Nome_produto} adicionado com sucesso!!! \n")

    elif Escolha_opcao == 2:
        Nome_produto = input("Escreva o nome do Produto que deseja atualizar: ")

        if Nome_produto in estoque:
            Preco = float(input("Digite o Valor do Produto: "))
            Quantidade = int(input("Digite a quantidade desejada: "))
            estoque[Nome_produto]= {"Preço": Preco, "Quantidade": Quantidade} 
            print(f"Produto {Nome_produto} foi atualizado")
        else:
            print("Produto não existe no estoque")

    elif Escolha_opcao == 3:
        Nome_produto = input("Nome do Produto que deseja Excluir:  ")
        if Nome_produto in estoque: 
            del estoque [Nome_produto]
            print(f"Produto {Nome_produto} excluído com sucesso!!")
        else:
            print(f"Produto {Nome_produto} não existe \n")
    elif Escolha_opcao == 4:
        print("Estoque Atual:")
        for produto, detalhes in estoque.items():
            print(f"Produto: {produto}, Preço: R$ {detalhes ['Preço']}, Quantidade: {detalhes ['Quantidade']}")

        while True:
             Sair = input("Deseja voltar ao Menu inicial? (S/N): ")
             if Sair.lower() in ["s", "n"]:
                      if Sair.lower() == "s":
                            break
                      else:
                            print("Fim do Menu!! Obrigado")
                            
    
    elif Escolha_opcao == 5:
         print("Fim do Menu \n")
         break



    else:
      print("Opção Invalida \n") 



