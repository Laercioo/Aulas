import pandas as pd

dados = {
    "nome":["João", "Marta", "Ary", "Matheus", "Michelle", "Larcio", "Alexandre"],
    "idade": [51,37,23,24,33,33,32],
    "cidade":["Recife", "Recife", "Recife", "Salvador", "Salvador", "São Paulo", "Manaus"],
}

df = pd.DataFrame(data=dados)

moradores_recife = df[df['cidade'] == 'Recife']

print(moradores_recife)