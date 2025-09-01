"""14. Usando abs()
Crie uma lista com os números [-5, 8, -2, 10]. Use um laço for para criar uma nova lista
contendo o valor absoluto (positivo) de cada número. Imprima a nova lista."""

# Lista original
numeros = [-5, 8, -2, 10]

# Lista para armazenar os valores absolutos
valores_absolutos = []

# Percorre a lista e aplica abs() em cada número
for n in numeros:
    valores_absolutos.append(abs(n))

print("Lista original:", numeros)
print("Lista com valores absolutos:", valores_absolutos)