def parimpar(matricula):
    if matricula % 2 == 0:
        return('Este número é PAR')
    else:
        return('Este número é IMPAR')

numeros_matricula = []

for i in range(5):
    numero = int(input(f'Digite o numero de matrícula: '))
    numeros_matricula.append(numero)

for numero in numeros_matricula:
    resultado = parimpar(numero)
    print(f'Número de matrícula {numero}: {resultado}')