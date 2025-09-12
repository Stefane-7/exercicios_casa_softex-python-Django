"""11. Calculadora de IMC: Crie uma função que receba o peso (em kg) e a altura (em metros)
e retorne o Índice de Massa Corporal (IMC). A fórmula é: IMC = peso / (altura ** 2)."""

def calcular_imc(peso: float, altura: float) -> float:
    imc = peso / (altura ** 2)
    return imc
  
def entrada_dados():
    while True:
        try:
            peso = float(input("Digite seu peso (kg): ").replace(",", "."))
            altura = float(input("Digite sua altura (m): ").replace(",", "."))
            return peso, altura
        except ValueError:
            print("Digite apenas números válidos.")
  
def executando():
    peso, altura = entrada_dados()
    imc = calcular_imc(peso, altura)
    print(f"O IMC referente aos dados digitados é {imc:.2f}")

executando()
