"""8. Conversão de Tipos: Crie uma lista cidades_lista = ['Paris', 'Londres', 'Tóquio']. Converta
essa lista para uma tupla. Depois, converta a tupla de volta para uma lista e adicione
'Nova York'."""


cidades_lista = ['Paris', 'Londres', 'Tóquio']
convertido_em_tupla = tuple(cidades_lista)
print(convertido_em_tupla)

novamente_lista = list(convertido_em_tupla)
novamente_lista.append('Nova York')

print(novamente_lista)
