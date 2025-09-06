"""13. Crie um dicionário que use tuplas como chaves. As chaves devem ser coordenadas (x, y)
e os valores, o nome de um local. Peça ao usuário para digitar as coordenadas e imprima
o local."""

mapa = {
    (0, 0): "Praça Central",
    (1, 2): "Supermercado",
    (3, 4): "Escola",
    (5, 1): "Hospital"
}

entrada = input("Digite uma coordenada: ")
for coordenada, local in mapa.items():
  if entrada == coordenada:
    print(f"O local correspondente é : {local}")
    break
  else:
    print(f"Não foi encontrada nenhuma correspondecia para: '{entrada}'")
    break
