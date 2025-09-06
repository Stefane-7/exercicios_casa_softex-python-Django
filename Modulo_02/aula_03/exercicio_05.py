"""5. Crie um dicionário com 3 produtos e suas quantidades em estoque. Peça ao usuário para
digitar um nome de produto e uma quantidade para adicionar. Atualize o estoque e
imprima o dicionário."""

"""5. Crie um dicionário com 3 produtos e suas quantidades em estoque. Peça ao usuário para
digitar um nome de produto e uma quantidade para adicionar. Atualize o estoque e
imprima o dicionário."""

estoque = {'cobertores': 10, 'lençóis': 15, 'toalhas': 7}
print(f"Estoque inicial: {estoque}")

while True:
    produto = input("Digite o produto a ser adicionado (ou 'parar' para encerrar): ").lower()
    if produto == "parar":
        break

    quantidade = int(input("Digite a quantidade: "))

    if produto in estoque:
        estoque[produto] += quantidade
    else:
        estoque[produto] = quantidade

    print(f"Estoque atualizado: {estoque}")

print("\nEstoque final:", estoque)