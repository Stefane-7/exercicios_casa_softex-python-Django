"""19. Palíndromo com reverse() e join()
Peça ao usuário para digitar uma palavra. Converta a palavra para uma lista de letras. Crie
uma cópia da lista e use .reverse(). Use .join() nas duas listas para formar as palavras.
Compare-as e imprima se a palavra original é um palíndromo (lida igual de trás para frente,
como "arara")."""

# Solicita uma palavra ao usuário
palavra = input("Digite uma palavra: ")

# Converte a palavra em lista de letras
lista_letras = list(palavra)

# Cria uma cópia da lista
lista_invertida = lista_letras.copy()

# Inverte a cópia
lista_invertida.reverse()

# Junta novamente em strings
original = "".join(lista_letras)
invertida = "".join(lista_invertida)

# Compara e verifica se é palíndromo
if original == invertida:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")