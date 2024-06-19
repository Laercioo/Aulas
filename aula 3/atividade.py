
#Criando tupla
linguagens_tupla = ('Java', 'Python', 'Goland')

#Tupla transformada em lista
linguagens_lista = list(linguagens_tupla)
print("Tupla transformada em lista")

print(type(linguagens_lista))

# Adicionando dois elementos com extend
linguagens_lista.extend("Malbolge", "Ruby")
print("Lista com dois dados adicionados")
print(linguagens_lista)