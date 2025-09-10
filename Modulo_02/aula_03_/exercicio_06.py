"""6. Crie um dicionário com 4 nomes e idades. Percorra o dicionário e imprima cada nome e
idade no formato "Nome: [Nome], Idade: [Idade]"""

usuarios = {'Maria': 21, 'Pedro': 30, 'Carlos': 25, 'Julia': 34}
for nome, idade in usuarios.items():
  print(f"Nome: {nome}, Idade: {idade}")