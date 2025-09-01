"""13. Conversão float()
Crie uma lista vazia. Peça ao usuário para digitar 3 preços. Use float() para converter os
valores e adicione-os à lista. Ao final, some todos os preços e imprima o valor total com 2
casas decimais."""

lista_numeros = []

for i in range(1,4):
  numeros = input(f"Digite o {i}° número: ")
  numeros = numeros.replace(",", ".")
  numeros = float(numeros)
  lista_numeros.append(numeros)
total = 0
for valor in lista_numeros:
  total += valor 
print(f"O valor total é R$ {total:.2f}".replace('.', ','))
   