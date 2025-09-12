"""9. Encontrar o Maior Número: Crie uma função que receba uma lista de números e
retorne o maior número da lista. Use um loop. Se a lista estiver vazia, retorne None."""

def maior_numero(lista: list) -> int | None:
    if not lista:   
        return None
    
    maior = lista[0]  
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior



print(maior_numero([5, 9, 2, 17, 3]))  
print(maior_numero([]))  