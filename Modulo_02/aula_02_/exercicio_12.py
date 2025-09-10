"""12. Diferença de Conjuntos: Ainda com os conjuntos do exercício 10, use o método
.difference() para encontrar os clientes que são premium mas não são recentes."""

clientes_premium = {'Maria','Pedro','Ana'}
clientes_recentes = {'Ana','João','Lucas'}
clientes_diferentes = clientes_premium.difference(clientes_recentes)

print(f"Clientes premium: {clientes_premium}")
print(f"Clientes recentes: {clientes_recentes}")
print(f"Apenas clientes premium: {clientes_diferentes}")