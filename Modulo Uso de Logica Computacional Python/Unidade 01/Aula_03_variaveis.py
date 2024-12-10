# Variaveis e tipos de dados

# 1 - O que é uma variável??
# È um espaço reservado na memoria, que serve para 
# armazenar qualquer tipo de dado.

# 2 - O que é tipagem dinâmica??
# Significa que não é necessario especificar, na 
# declaração, o tipo de variavel.

# Exemplo de nome de variavel (snake case)
nome_aluno = "Fernando"
nota_aluno = 8 


# 3 - Quais os tipód de dados em Python??
#Inteiro (int), Decimal (float), Complexo (comples),
#String (str), Boolean (bool), List, tuple, sets e dictionary

#Exemplo: 

ano_atual = 2023
desconto = 15.59
cidade = "Goianesia"
filhos = False
cores = ["branco", "azul", "vermelho"]
frutas = ("banana", "uva")
notas = {5, 10, 30}
cliente = {
    "nome":"Maria",
    "altura": "1.95",
    "peso": 60.00
}

# 4 - O que é tipagem forte?? Não deixar alterar o tipo de dado

numero1 = 23
numero2 = 100
print (numero1 + numero2)

# 5 - Como trocar o tipo de variavel??
preco_produto = 1.90
preco_produto = str(preco_produto)
preco_produto = float(preco_produto)

print (type (preco_produto))