"""12. Classificador de IMC: Baseado no exercício anterior, crie uma função que receba o IMC
e retorne a classificação: "Abaixo do peso", "Peso normal", "Sobrepeso" ou "Obesidade".
Use múltiplos if/elif/else."""

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
    
    if imc <  18.05:
      print("Abaixo do peso")
    elif imc >= 18.05 and imc <= 24.9: 
      print("Peso normal")
    elif imc >= 20.00 and imc <= 29.9:
      print("Sobrepeso")
    else:
      print("Obesidade")
      



executando()