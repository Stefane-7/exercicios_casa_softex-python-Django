"""20. Vendas Simples: Crie um dicionário de estoque e outro de vendas. Simule uma venda,
diminuindo a quantidade no estoque e adicionando a venda ao dicionário de vendas. Use
if para garantir que há estoque suficiente."""


estoque = {
    "camiseta": 10,
    "calça": 5,
    "sapato": 3
}


vendas = {}

produto = input("Digite o nome do produto: ").lower()
quantidade = int(input("Digite a quantidade que deseja comprar: "))


if produto in estoque:
    if estoque[produto] >= quantidade:
        estoque[produto] -= quantidade  
        
        if produto in vendas:
            vendas[produto] += quantidade
        else:
            vendas[produto] = quantidade
        
        print(f"Venda realizada! Estoque restante de {produto}: {estoque[produto]}")
    else:
        print("Quantidade indisponível no estoque.")
else:
    print("Produto não encontrado.")

print("\nEstoque final:", estoque)
print("Vendas realizadas:", vendas)