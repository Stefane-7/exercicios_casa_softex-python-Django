"""14. Dada uma lista de palavras, crie um dicionário que conte a frequência de cada palavra."""


palavras = ["gato", "cachorro", "gato", "pássaro", "gato", "cachorro"]

frequencia = {}  

for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1  
    else:
        frequencia[palavra] = 1

print(frequencia)