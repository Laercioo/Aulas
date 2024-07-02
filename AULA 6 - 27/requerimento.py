import requests

squad = {
    "André": "11630-067",
    "Luis": "11634-060",
    "Laercio": "11630-135",
    "Nicolas": "11630-065"
}

nome = input("Digite o nome do integrante: ")
cep = input("Digite o CEP da cidade do integrante: ")

squad[nome] = cep

resultado = {}

for nome, cep in squad.items():
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    
    if response.status_code == 200:
        data = response.json()
        cidade = data.get("localidade")
        resultado[nome] = cidade 
    
for nome, cidade in resultado.items():
    print(f'A cidade do integrante {nome} é {cidade}')

with open ("requeriment.txt", "w") as f:
    f.write("requests\n")
    
    print(resultado)