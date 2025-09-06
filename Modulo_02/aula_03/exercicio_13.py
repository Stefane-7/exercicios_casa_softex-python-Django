"""13. Crie um dicionário que use tuplas como chaves. As chaves devem ser coordenadas (x, y)
e os valores, o nome de um local. Peça ao usuário para digitar as coordenadas e imprima
o local."""

mapa = {
    (0, 0): "Praça Central",
    (1, 2): "Supermercado",
    (3, 4): "Escola",
    (5, 1): "Hospital"
}

entrada = input("Digite uma coordenada no formato x,y: ")

try:
    x, y = map(int, entrada.split(','))
    coordenada = (x, y)
    
    if coordenada in mapa:
        print(f"O local correspondente é: {mapa[coordenada]}")
    else:
        print(f"Não foi encontrada nenhuma correspondência para: {coordenada}")
except ValueError:
    print("Entrada inválida! Digite no formato x,y com números inteiros.")
