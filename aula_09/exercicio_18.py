"""18. Encontrando o Maior Valor
Crie uma lista de números. Use um laço for para encontrar e imprimir o maior número da lista
sem usar a função max()."""

numeros = [10, 50, 25, 30, 90]
maior = numeros[0]
for num in numeros:
   if num > maior:
     maior = num
     
print(maior)