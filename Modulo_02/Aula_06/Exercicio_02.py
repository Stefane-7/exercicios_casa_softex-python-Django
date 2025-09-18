"""Exercício 2: Criando Pessoas Reais
Usando a classe Pessoa que você criou, crie dois objetos:
1. Uma pessoa chamada "João", com 25 anos.
2. Uma pessoa chamada "Maria", com 30 anos.
Depois de criá-los, imprima o nome e a idade de cada um para confirmar que deu certo."""

class Pessoa:
  def __init__(self, nome: str, idade: int) -> None:
    self.nome = nome
    self.idade = idade

joao = Pessoa("João", 25)
maria = Pessoa("Maria", 30)

print(f"Olá, eu me chamo {joao.nome} e tenho {joao.idade} anos!")
print(f"Olá, eu me chamo {maria.nome} e tenho {maria.idade} anos!")