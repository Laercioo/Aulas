# Criando uma tupla com 5 dados
dados_tupla = ("Laranja", "Maçã", "Banana", "Uva", "Melancia")

# Convertendo a tupla para uma lista
dados_lista = list(dados_tupla)

# Inserindo 2 dados extras na lista
dados_lista.append("Morango")
dados_lista.append("Abacaxi")

# Removendo o primeiro dado da lista
dados_lista.remove("Laranja")

# Removendo o último dado da lista
dados_lista.pop()

# Imprimindo o primeiro dado da lista
primeiro_dado = dados_lista[0]
print(f"Primeiro dado da lista: {primeiro_dado}")

# Imprimindo a quantidade de dados da lista
quantidade_dados = len(dados_lista)
print(f"Quantidade de dados na lista: {quantidade_dados}")

# Criando um dicionário com dados de Nome, Idade e Profissão
pessoa = {"Nome": "João", "Idade": 30, "Profissão": "Programador"}

# Imprimindo o valor contido na chave Nome do dicionário
nome_pessoa = pessoa["Nome"]
print(f"Nome da pessoa: {nome_pessoa}")