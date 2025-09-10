"""4. Crie um dicionário com os nomes de 3 países e suas capitais. Peça ao usuário para
digitar o nome de um país e imprima a capital correspondente. Use dicionario.get() para
evitar erros."""

paises_e_capitais = {'brasil': 'brasilia', 'japão': 'tokyo', 'frança': 'paris'}
pais = input("Digite o nome de um país: ")
capital = paises_e_capitais.get(pais)
if capital:
  print(f"A capital do país: {pais.title()} é: {capital.title()}")
else:
  print("País não encotrado")
