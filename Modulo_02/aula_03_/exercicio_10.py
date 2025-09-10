"""10. Crie um dicionário com cores e seus códigos hexadecimais. Use um loop while para
permitir que o usuário procure o código de uma cor repetidamente. O loop deve terminar
quando o usuário digitar "sair"."""

cores = {
    "preto": "#000000",
    "branco": "#FFFFFF",
    "vermelho": "#FF0000",
    "verde": "#00FF00",
    "azul": "#0000FF",
    "amarelo": "#FFFF00",
    "ciano": "#00FFFF",
    "magenta": "#FF00FF",
    "laranja": "#FFA500",
    "rosa": "#FFC0CB",
    "roxo": "#800080",
    "marrom": "#A52A2A",
    "cinza": "#808080",
    "turquesa": "#40E0D0",
    "dourado": "#FFD700"
}

while True:
    entrada = input("Digite o código correspondente a cor que deseja(ou 'sair' para parar): ").upper()
    if entrada == 'sair':
      print("Encerrando...")
      break
    encontrado = False
    for cor, codigo in cores.items():
      if entrada == codigo:
        print(f"A cor correspondente ao codigo digitado é: {cor}")
        encontrado = True
        break
    if not encontrado:
        print(f"Nenhuma correspondencia encontrada para o código digitado: '{entrada}' ")
  
      
