def calcular(num1, num2, operacao):
  if operacao == '+':
      return num1 + num2
  elif operacao == '-':
      return num1 - num2
  else:
      return "Operação inválida"

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (soma ou subtracao): ").strip().lower()

resultado = calcular(numero1, numero2, operacao)
print("O resultado é:", resultado)