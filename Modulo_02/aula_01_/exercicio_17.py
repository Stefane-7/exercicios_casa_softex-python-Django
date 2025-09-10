"""17. Fila com while
Crie uma fila de atendimento com 3 nomes. Use um laço while para "atender" um cliente de
cada vez (pop(0)) e imprima quem está sendo atendido a cada passo. O laço deve continuar
enquanto houver clientes na fila."""

pacientes = ['Maria', 'Pedro', 'Carla']

while pacientes:
  em_atendimento = pacientes.pop(0)
  print(f"Paciente em atendimento: {em_atendimento}")