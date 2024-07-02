import requests

estado_desconto = ["AL","BA","CE","MA","PE","PI","RN","SE","AC","AP","AM","PA","RO","RR","TO"]
cep = input("Favor digitar seu cep. ")

def verificaestado(estado):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/') 
    data = response.json()
    estado = data["uf"]
                
    return estado in estado_desconto

if verificaestado(cep):
    print("O CEP inserido é elegível para frete grátis")
    
else:
    print("O CEP inserido não é elegível para frete grátis.")