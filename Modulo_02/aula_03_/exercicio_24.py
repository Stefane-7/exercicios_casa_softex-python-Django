"""24. Sistema de Inventário: Crie um dicionário de inventário de um jogo (ex: "espada":
{"dano": 50, "peso": 2.5}). Permita que o usuário insira um item no inventário com suas
características e liste todos os itens."""


inventario = {
    "Espada": {"dano": 50, "peso": 2.5},
    "Arco": {"dano": 35, "peso": 1.5},
    "Escudo": {"dano": 10, "peso": 5.0}
}

while True:
    print("\nSistema de Inventário")
    print("1. Adicionar item")
    print("2. Listar itens")
    print("3. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome = input("Nome do item: ")
        dano = input("Dano do item: ")
        peso = input("Peso do item: ")

        inventario[nome] = {"dano": float(dano), "peso": float(peso)}
        print(f"Item '{nome}' adicionado com sucesso!")

    elif escolha == "2":
        if inventario:
            print("\nItens no inventário:")
            for item, caracteristicas in inventario.items():
                print(f"{item}: Dano = {caracteristicas['dano']}, Peso = {caracteristicas['peso']}")
        else:
            print("O inventário está vazio.")

    elif escolha == "3":
        print("Saindo do sistema de inventário...")
        break

    else:
        print("Opção inválida! Tente novamente.")