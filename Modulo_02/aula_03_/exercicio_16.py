"""16. Inversão de Dicionário: Crie um dicionário. Troque as chaves pelos valores e os valores
pelas chaves. Dica: Os valores devem ser únicos para que isso funcione."""

dicionario = {
    "brasil": "brasilia",
    "frança": "paris",
    "japão": "tokyo"
}

dicionario_invertido = {}

for chave, valor in dicionario.items():
    dicionario_invertido[valor] = chave

print("Dicionário original:", dicionario)
print("Dicionário invertido:", dicionario_invertido)

