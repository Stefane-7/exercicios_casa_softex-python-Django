"""19. Ordenador de Dicionários com lambda: Crie uma função que receba uma lista de
dicionários (cada um com "nome" e "idade"). Use uma lambda e um loop para ordenar a
lista pela idade e retornar a lista ordenada."""

def ordenar_dicionarios(lista: list[dict]) -> list[dict]:
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j]["idade"] > lista[j + 1]["idade"]:
              
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista



pessoas = [
    {"nome": "Beatriz", "idade": 30},
    {"nome": "Ana", "idade": 25},
    {"nome": "Carlos", "idade": 19}
]

print("Antes de ordenar:")
print(pessoas)

ordenadas = ordenar_dicionarios(pessoas)

print("\nDepois de ordenar:")
print(ordenadas)