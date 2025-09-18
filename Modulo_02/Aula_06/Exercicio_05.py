"""Exercício 5: Conta Bancária
Crie uma classe ContaBancaria. Toda conta deve começar com um titular e um saldo inicial.
Crie um método depositar(valor) que some um valor ao saldo da conta. Crie um objeto,
deposite um valor e imprima o novo saldo."""

class ContaBancaria:
  def __init__(self, titular: str, saldo: float) -> None:
    self.titular = titular 
    self.saldo = saldo
    
  def depositar(self, valor: float) -> None:
    if valor > 0:
      self.saldo += valor
    
    else:
      print("Valor inválido para depósito")
      

usuario_1 = ContaBancaria("Luiz", 250.55)

usuario_1.depositar(150)

print(f"Novo saldo de {usuario_1.titular}: R$ {usuario_1.saldo:.2f}")