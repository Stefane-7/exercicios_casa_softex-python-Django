"""21. Validador de Entrada Numérica: Crie uma função que solicite ao usuário que digite um
número inteiro. Use um loop e try/except para garantir que a entrada seja válida. A
função deve retornar o número inteiro."""

def entrada_numerica() -> int:
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
            
num = entrada_numerica()
print(f"Você digitou o número: {num}")