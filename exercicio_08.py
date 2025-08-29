"""8. Adicionando com while
Crie uma lista vazia. Use um laço while para pedir ao usuário que adicione 3 nomes à lista. Ao
final, imprima a lista."""

lista = []
contador = 0
while contador < 3:
  nomes = input("Digite um nome: ")
  lista.append(nomes)
  contador += 1
  
print(lista)
  