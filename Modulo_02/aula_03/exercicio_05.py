"""5. Crie um dicionário com 3 produtos e suas quantidades em estoque. Peça ao usuário para
digitar um nome de produto e uma quantidade para adicionar. Atualize o estoque e
imprima o dicionário."""

"""5. Crie um dicionário com 3 produtos e suas quantidades em estoque. Peça ao usuário para
digitar um nome de produto e uma quantidade para adicionar. Atualize o estoque e
imprima o dicionário."""

estoque = {'cobertores': 10, 'lençois': 15, 'toalhas': 7}
print(estoque)
produto = input("Digite o produto a ser adicionado no estoque: ")
quantidade = int(input("Digite a quantidade: "))

estoque[produto] = quantidade

print(f"Estoque após atualização: {estoque}")