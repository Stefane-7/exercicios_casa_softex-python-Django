"""15. Crie um dicionário com os nomes de 3 pessoas e seus hobbies (em formato de conjunto).
Peça ao usuário para digitar o nome de uma pessoa e imprima seus hobbies."""

# Criando o dicionário com nomes e hobbies
pessoas = {
    "Maria": {"ler", "cantar", "nadar"},
    "João": {"jogar futebol", "cozinhar", "viajar"},
    "Ana": {"desenhar", "assistir filmes", "dançar"}
}

nome = input("Digite o nome da pessoa: ").capitalize()


if nome in pessoas:
    print(f"Hobbies de {nome}: {pessoas[nome]}")
else:
    print("Nome não encontrado.")