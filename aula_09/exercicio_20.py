"""20. Manipulando input() e split()
Peça ao usuário para digitar uma lista de 5 frutas separadas por vírgula (ex:
"maçã,banana,uva,morango,kiwi"). Use o método .split(',') para transformar a string em uma
lista. Imprima a lista de frutas e o total de frutas que o usuário digitou."""

entrada = input("Digite 5 frutas separadas por vírgula: ")

frutas = entrada.split(",")

frutas = [fruta.strip() for fruta in frutas]

print("Lista de frutas:", frutas)
print("Total de frutas digitadas:", len(frutas))