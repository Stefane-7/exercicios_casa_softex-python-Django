"""11. Calculadora de IMC: Crie uma função que receba o peso (em kg) e a altura (em metros)
e retorne o Índice de Massa Corporal (IMC). A fórmula é: IMC = peso / (altura ** 2)."""

def calcular_imc(peso: float, altura: float) -> float | None:
  imc = peso / (altura ** 2)
  return imc
  
def entrada_dados():
  try:
    peso = float(input("Digite seu peso: "))#.replace(",", ".")
    altura = float(input("Digite sua altura: "))#.replace(",", ".")
  except ValueError:
    print("Digite apenas números.")
    return peso, altura
def executando():
  peso, altura = entrada_dados()
  imc = calcular_imc(peso, altura)
  
  print(f"O IMC referente aos dados digitados é {imc}")

executando()