"""10. União de Conjuntos: Você tem dois conjuntos de clientes: clientes_premium = {'Maria',
'Pedro', 'Ana'} e clientes_recentes = {'Ana', 'João', 'Lucas'}. Use o método .union() para
criar um novo conjunto com todos os clientes."""



clientes_premium = {'Maria','Pedro','Ana'}
clientes_recentes = {'Ana','João','Lucas'}

todos_os_clientes = clientes_premium.union(clientes_recentes)
print(clientes_premium)
print(clientes_recentes)
print(todos_os_clientes)
