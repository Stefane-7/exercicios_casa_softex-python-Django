"""7. Encontrando um Item
Crie uma lista com 5 itens. Peça ao usuário para digitar um item. Use o método .count() para
verificar e imprimir quantas vezes esse item aparece na lista."""

itens = ["carregador", "chapeu", "espelho", "óculos", "celular"]
usuario = input("Digite um item da lista: ")
quantidade = itens.count(usuario)
print(f"O item {usuario}, aparece {quantidade} vez(es) na lista.")
