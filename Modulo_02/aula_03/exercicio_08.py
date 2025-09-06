"""8. Crie um dicionário com produtos e preços. Peça ao usuário para digitar um produto para
remover. Remova-o do dicionário e imprima o dicionário final. Use if para verificar se o
produto existe antes de remover."""

produtos = {'celular': 150.00, 'relogio': 90.00, 'tela': 70.00}
remover = input("Digite o item a ser removido: ").lower()
if remover in produtos: 
  produto_removido = produtos.pop(remover)
  print(f"Produto removido do estoque: {remover} - R$: {produto_removido:.2f}")
  print(f"\nEstoque atualizado: {produtos}")
else:
  print("Produto não encontrado no estoque.")
  print(f"\nEstoque atual: {produtos}")