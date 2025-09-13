"""15. Soma de Números Variáveis: Crie uma função que use *args para somar uma
quantidade qualquer de números."""

def soma_numeros(*numeros: float) -> float:
    """Soma qualquer quantidade de números passados como argumentos."""
    return sum(numeros)

def entrada_dados() -> list[float]:
    """Solicita ao usuário que digite números separados por espaço e retorna uma lista de floats, validando a entrada."""
    while True:
        numeros_str = input("Digite os números separados por espaço ou virgula: ").replace(",", " ")
        try:
            numeros = [float(num) for num in numeros_str.split()]
            return numeros
        except ValueError:
            print("Erro: Certifique-se de digitar apenas números separados por espaço ou virgula.")

def executar_soma():
    """Função que une entrada de dados e soma dos números."""
    numeros = entrada_dados()
    resultado = soma_numeros(*numeros)
    print(f"A soma dos números é: {resultado}")

executar_soma()