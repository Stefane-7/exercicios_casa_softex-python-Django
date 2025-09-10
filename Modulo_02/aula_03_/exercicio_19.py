"""19. Análise de Dados: Dada uma lista de dicionários de produtos (com nome e preço),
encontre e imprima o nome e o preço do produto mais caro."""

produtos = [
    {"nome": "Celular", "preco": 1500},
    {"nome": "Notebook", "preco": 3500},
    {"nome": "Relógio", "preco": 800},
    {"nome": "TV", "preco": 2200}
]

mais_caro = produtos[0]  

for produto in produtos:
    if produto["preco"] > mais_caro["preco"]:
        mais_caro = produto

print(f"Produto mais caro: {mais_caro['nome']} - R$ {mais_caro['preco']}")