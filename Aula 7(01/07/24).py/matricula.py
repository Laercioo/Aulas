numbers = []

while len(numbers) < 5:
    matricula = input("Digite o número de matrícula: ")
    numbers.append(matricula)

def verificar_par_impar(number):
    if number % 2 == 0:
        return "par"
    else:
        return "ímpar"

for number in numbers:
    resultado = verificar_par_impar(int(number))
    print(f"O número {number} é {resultado}.")