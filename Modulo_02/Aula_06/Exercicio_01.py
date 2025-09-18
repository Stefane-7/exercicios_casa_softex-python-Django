"""   Exercício 1: Molde de uma Pessoa

Crie uma classe chamada Pessoa. 
No "registro de nascimento" (__init__), toda pessoa deve ter um nome e uma idade."""

class Pessoa:
  def __init__(self, nome: str, idade: int) -> None:
    self.nome = nome
    self.idade = idade

pessoa = Pessoa("Paula", "33")    

print(pessoa.nome)
print(pessoa.idade)