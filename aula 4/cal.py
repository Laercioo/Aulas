def calculadora():
  """
  Calculadora using match-case for Python 3.10 or higher.

  This improved version incorporates error handling, user-friendly guidance,
  and potential enhancements for a more robust experience.

  Args:
    None

  Returns:
    None
  """

  # Get numbers from the user
  while True:
    try:
      num1 = float(input("Digite o primeiro número: "))
      num2 = float(input("Digite o segundo número: "))
      break  # Exit the loop if numbers are valid
    except ValueError:
      print("Entrada inválida. Digite apenas números.")

  # Get operation from the user
  while True:
    operacao = input("Digite a operação (+, -, *, /): ").strip()
    if operacao in "+-*/":
      break  # Exit the loop if operation is valid
    else:
      print("Operação inválida. Digite +, -, *, ou /.")

  # Calculate result using match-case (requires Python 3.10+)
  resultado = match operacao:
    case "+":
      return soma(num1, num2)
    case "-":
      return subtracao(num1, num2)
    case "*":
      return multiplicacao(num1, num2)
    case "/":
      if num2 == 0:
        print("Erro: Divisão por zero!")
        return None  # Indicate error for further handling
      else:
        return divisao(num1, num2)
    case _:
      print("Operação inválida!")
      return None  # Indicate error or provide alternative options

# Functions for mathematical operations
def soma(num1, num2):
  return num1 + num2

def subtracao(num1, num2):
  return num1 - num2

def multiplicacao(num1, num2):
  return num1 * num2

def divisao(num1, num2):
  return num1 / num2

# Main program execution
if __name__ == "__main__":
  calculadora()

  # Potential enhancements (optional):
  # - Add more operations (e.g., exponentiation, modulo)
  # - Create a loop for continuous calculations
  # - Implement a graphical user interface (GUI)
