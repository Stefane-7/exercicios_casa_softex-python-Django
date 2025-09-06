"""7. Usando o dicionário do exercício anterior, imprima apenas os nomes. Depois, imprima
apenas as idades."""

usuarios = {'Maria': 21, 'Pedro': 30, 'Carlos': 25, 'Julia': 34}
for nome, idade in usuarios.items():
  print(f"Nome: {nome}")
print("#_#" * 30)
for nome, idade in usuarios.items():
  print(f"\nNome: {idade}")