"""18. União de Dicionários: Crie dois dicionários. Crie um terceiro dicionário que seja a união
dos dois primeiros. Se uma chave existir em ambos, use o valor do segundo dicionário."""


dicionario1 = {"a": 1, "b": 2, "c": 3}
dicionario2 = {"b": 20, "d": 4}


uniao = dicionario1.copy()  
uniao.update(dicionario2)   

print(uniao)