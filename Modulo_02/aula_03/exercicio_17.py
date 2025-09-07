"""17. Criação com Condição: Crie um dicionário a partir de uma lista de números, onde a
chave é o número e o valor é "par" ou "ímpar"."""

numeros = [1, 2, 3, 4, 5, 6]

paridade = {}  

for n in numeros:
    if n % 2 == 0:
        paridade[n] = "par"
    else:
        paridade[n] = "ímpar"

print(paridade)