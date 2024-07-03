import pandas as pd

dados = pd.read_csv('./dados_ficticios.csv')

dados = {
    "nome":["Rafaela Rezende",
            "Srta. Beatriz das Neves",
            "Ana Clara das Neves",
            "Olivia Silva",
            "Alexia Martins",
            ],
    
    endereço:[
        "Avenida de Ribeiro Santa Helena 14342136 Caldeira das Pedras / SP",
        "Loteamento de Fogaça, 61 Vila Novo São Lucas 11233-022 Monteiro / SC",
        "Favela Pinto, 97 São José 60325-119 Rodrigues / MS",
        "Vereda de Duarte, 12 Vila Satélite 91893-339 Souza / RN",
        "Conjunto João Pedro Caldeira, 888 Sion 81988-738 Azevedo da Mata / MA"
        
        ]
    e-mail:[
        "mouraheitor@example.org",
        "luiz-otaviocorreia@example.org",
        "isisalmeida@example.org",
        "lpeixoto@example.org",
        'carvalhoana-beatriz@example.com',
        
    ]
    "idade":[
         46,
         24,
         28,
         23,
         54,
         
         
         ],
    
    "Renda":[
        15594.52, 
        16478.26,
        13729.48,
        18478.46,
        9988.47,
        
        ]
}

df = pd.DataFrame(data=dados)

print(df)[df['idade'] > 40]
print(df)[df['renda'] > 5.000]
print(df)[df['renda'] > 15.000]