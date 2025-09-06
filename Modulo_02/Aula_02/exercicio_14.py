"""14. Processando Registros de Logs: Você tem uma lista de tuplas de acessos a um site:
logs = [('192.168.1.1', '2023-01-01'), ('10.0.0.2', '2023-01-02'), ('192.168.1.1', '2023-01-03')].
Crie um conjunto para armazenar todos os endereços IP únicos."""


logs = [('192.168.1.1', '2023-01-01'), ('10.0.0.2', '2023-01-02'), ('192.168.1.1', '2023-01-03')]
ip = set()
for i, d in logs:
  ip.add(i)
  
print(ip)
  