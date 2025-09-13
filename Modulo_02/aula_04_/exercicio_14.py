"""14. Gerador de Fibonacci: Crie uma função que receba um número inteiro n e retorne uma
lista com a sequência de Fibonacci até o n-ésimo termo."""
def fibonacci(n: int) -> list[int]:
    sequencia = []
    a, b = 0, 1
    for _ in range(n):
        sequencia.append(a)
        a, b = b, a + b
    return sequencia


def entrada_dados():
    try:
        n = int(input("Digite um número inteiro para gerar a sequência de Fibonacci: "))
        resultado = fibonacci(n)
        print(f"A sequência de Fibonacci \ncom {n} termos é: \n{resultado}")
    except ValueError:
        print("Por favor, digite apenas números inteiros.")


entrada_dados()
