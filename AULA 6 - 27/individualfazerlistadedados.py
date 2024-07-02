import os

# Criar uma lista de dados
dados = ['Item 1', 'Item 2', 'Item 3']

# Interagir com o sistema operacional usando a biblioteca OS
print("Diretório atual:", os.getcwd())  # Exibir o diretório atual
print("Lista de arquivos e pastas no diretório atual:")
for item in os.listdir():
    print(item)  # Exibir todos os itens do diretório atual

# Criar uma nova pasta
nova_pasta = 'nova_pasta'
if not os.path.exists(nova_pasta):  # Verificar se a pasta já existe
    os.mkdir(nova_pasta)  # Criar a nova pasta
    print(f"A pasta ")