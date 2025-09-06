"""12. Conversão int()
Crie uma lista vazia. Peça ao usuário para digitar 3 números. Lembre-se que input() retorna
texto! Use int() para converter os números para o tipo correto e adicione-os à lista. Imprima a
lista no final."""

numeros_lista = []
for i in range(1,4):
  numeros = int(input(f"Digite o {i}° número: "))
  numeros_lista.append(numeros)
print(numeros_lista)
