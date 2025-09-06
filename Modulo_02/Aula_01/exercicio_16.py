"""16. Fila com pop() e append()
Crie uma lista para ser uma fila de atendimento (['cliente1', 'cliente2', 'cliente3']). Use append()
para adicionar um novo cliente e pop(0) para "atender" o primeiro cliente da fila. Imprima a
lista após cada operação."""

# Criando a fila
fila = ['cliente1', 'cliente2', 'cliente3']
print("Fila inicial:", fila)

# Adicionando um novo cliente ao final da fila
fila.append('cliente4')
print("Fila após novo cliente entrar:", fila)

# Atendendo o primeiro cliente da fila (remove o índice 0)
fila.pop(0)
print("Fila após atender o primeiro cliente:", fila)