"""Exercício 6: Lógica no Saque
Na mesma classe ContaBancaria, adicione um método para sacar(valor). Este método deve
verificar se há saldo suficiente na conta.
● Se houver, ele deve subtrair o valor do saldo e imprimir "Saque realizado com sucesso.".
● Se não houver, ele deve imprimir "Saldo insuficiente." e não alterar o saldo.
Teste os dois cenários: um saque bem-sucedido e uma tentativa de sacar mais do que
tem."""

class ContaBancaria:
  def __init__(self, titular: str, saldo: float) -> None:
    self.titular = titular 
    self.saldo = saldo
    
  def depositar(self, valor: float) -> None:
    if valor > 0:
      self.saldo += valor
    
    else:
      print("Valor inválido para depósito")
  
  def sacar(self, valor: float) -> None:
    if valor <= self.saldo:
      self.saldo -= valor
      print(f"Saque realizado com sucesso!")
    else:
      print("Saldo insuficiente.")
      

usuario_1 = ContaBancaria("Luiz", 250.55)

usuario_1.depositar(150)
usuario_1.sacar(400.55)
print(f"Novo saldo de {usuario_1.titular}: R$ {usuario_1.saldo:.2f}")