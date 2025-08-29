"""3. Apagando com .remove()
Crie uma lista com 3 cores. Peça ao usuário para digitar uma cor da lista para ser removida.
Remova a cor e imprima a lista atualizada."""

lista = ["azul", "vermelho", "amarelo"]
print(lista)
cor_a_remover = input("Digite uma cor a ser removida: ").lower()
lista.remove(cor_a_remover)
print(lista)