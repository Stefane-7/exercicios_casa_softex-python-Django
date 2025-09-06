"""19. Análise de Dados de Vendas: Você tem uma lista de vendas, onde cada venda é uma
tupla (produto, valor).
vendas = [('teclado', 150), ('mouse', 80), ('teclado', 150)]
Calcule o valor total de vendas. Em seguida, use um conjunto para contar quantos tipos
de produtos diferentes foram vendidos."""


vendas = [('teclado', 150), ('mouse', 80), ('teclado', 150)]

produtos = set()
total = 0 
for produto, valor in vendas:
  total += valor
  produtos.add(produto)
  
print(f"Produtos vendidos: {produtos}")
print(f"Valor total da vendas: R$ {total:.2f}")