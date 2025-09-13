"""17. Combinador de Argumentos: Crie uma função que receba um argumento obrigatório
(nome) e use *args e **kwargs para exibir todos os dados de forma clara."""

def combinador_argumentos(nome: str, *args, **kwargs) -> None:
    print(f"Nome: {nome}")
    
    if args:
        print("Args adicionais:")
        for i, arg in enumerate(args, start=1):
            print(f"  {i}. {arg}")
    else:
        print("Sem args adicionais.")
    
    if kwargs:
        print("Detalhes adicionais (kwargs):")
        for chave, valor in kwargs.items():
            print(f"  {chave}: {valor}")
    else:
        print("Sem kwargs adicionais.")

# Exemplo de uso:
combinador_argumentos(
    "Stefane",
    "Engenheira", "São Paulo",
    idade=28, profissão="Programadora"
)