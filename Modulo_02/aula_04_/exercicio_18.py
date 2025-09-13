"""18. Filtro de Lista com lambda: Crie uma função que receba uma lista de números e use
um loop para retornar uma nova lista apenas com os números pares. Use uma lambda
dentro do loop"""

def filtrar_pares(numeros):
    resultado = []
    eh_par = lambda x: x % 2 == 0 
    for n in numeros:
        if eh_par(n):
            resultado.append(n)
    return resultado

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = filtrar_pares(lista)
print(pares)  