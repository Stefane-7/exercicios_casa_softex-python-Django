"""15. Comparação de Inventário: Você tem uma tupla de itens do seu estoque estoque =
('camisa', 'calça', 'sapato') e uma lista de itens que foram vendidos vendidos = ['camisa',
'meia', 'calça']. Use conjuntos para encontrar os itens que foram vendidos mas ainda
estão no estoque."""


estoque = ('camisa', 'calça', 'sapato')
vendidos = ['camisa', 'meia', 'calça']

conjunto_estoque = set(estoque)
conjunto_vendidos = set(vendidos)
em_ambos = conjunto_vendidos.intersection(conjunto_estoque)

print(f"Os itens vendidos que ainda estão no estoque são: {em_ambos}")