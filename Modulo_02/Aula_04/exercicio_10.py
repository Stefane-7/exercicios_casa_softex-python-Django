"""10. Contador de Vogais: Crie uma função que receba uma string e retorne o número de
vogais (a, e, i, o, u) que ela contém."""

def contador_de_vogais(texto: str) -> int:
    vogais = "aeiouAEIOU"  
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador


print(contador_de_vogais("o rato roeu a roupa do rei de roma "))  