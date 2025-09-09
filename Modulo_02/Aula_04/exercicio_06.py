"""6. Cálculo de Média: Crie uma função que receba três notas e retorne a média delas."""

def verificador_de_media(n1: int, n2: int, n3: int) -> float:
  media = (n1 + n2 + n3) / 3
  return media
resultado = verificador_de_media(26, 28, 53)
print(f"A média das idades é: {resultado:.2f}")
  