"""22. Sistema de Pontuação: Crie um dicionário de jogadores e suas pontuações iniciais.
Simule uma rodada de jogo, atualizando a pontuação de um jogador específico. Permita
que o usuário adicione novos jogadores e pontue-os."""


pontuacoes = {
    "Alice": 10,
    "Bob": 15,
    "Carol": 20
}

while True:
    print("\n=== Sistema de Pontuação ===")
    print("1. Atualizar pontuação de um jogador")
    print("2. Adicionar novo jogador")
    print("3. Ver pontuações")
    print("4. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        jogador = input("Digite o nome do jogador: ")
        if jogador in pontuacoes:
            pontos = int(input("Quantos pontos adicionar? "))
            pontuacoes[jogador] += pontos
            print(f"{jogador} agora tem {pontuacoes[jogador]} pontos.")
        else:
            print("Jogador não encontrado.")
    
    elif escolha == "2":
        nome = input("Nome do novo jogador: ")
        if nome in pontuacoes:
            print("Este jogador já existe.")
        else:
            pontos_iniciais = int(input("Pontuação inicial: "))
            pontuacoes[nome] = pontos_iniciais
            print(f"{nome} adicionado com {pontos_iniciais} pontos.")
    
    elif escolha == "3":
        print("\nPontuações atuais:")
        for jogador, pontos in pontuacoes.items():
            print(f"{jogador}: {pontos} pontos")
    
    elif escolha == "4":
        print("Saindo do sistema...")
        break
    
    else:
        print("Opção inválida, tente novamente.")