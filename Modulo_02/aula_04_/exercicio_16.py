"""16. Detalhes do Produto: Crie uma função que receba o nome de um produto e use
**kwargs para exibir detalhes adicionais como preço, marca e estoque."""

def detalhes_produto(nome: str, **kwargs) -> None:
    print(f"Produto: {nome}")
    if not kwargs:
        print("Nenhum detalhe adicional fornecido.")
    else:
        for chave, valor in kwargs.items():
            print(f"{chave.capitalize()}: {valor}")

# Exemplo de uso:
detalhes_produto("Smartphone", preco=1500.0, marca="Samsung", estoque=20)
detalhes_produto("Caderno")  # Sem detalhes adicionais