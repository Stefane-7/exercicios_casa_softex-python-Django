"""Exercício 9: Atributo da Classe (Funcionários da Empresa)
Crie uma classe Funcionario. Cada funcionário terá nome e salário (atributos de instância).
Agora, crie um atributo de classe chamado percentual_bonus, com o valor 1.10
(representando 10% de bônus).
Crie um método aplicar_bonus que multiplica o salário do funcionário pelo percentual_bonus
da classe. Crie dois funcionários com salários diferentes, aplique o bônus e veja o resultado.
● Dica: Um atributo de classe é definido diretamente dentro da classe, fora de qualquer
método."""


class Funcionario:
    percentual_bonus = 1.10  

    def __init__(self, nome: str, salario: float) -> None:
        self.nome = nome
        self.salario = salario

    def aplicar_bonus(self) -> None:
        bonus = Funcionario.percentual_bonus
        salario = self.salario
        salario_com_bonus = salario * bonus
        self.salario = salario_com_bonus



f1 = Funcionario("Ana", 2000)
f2 = Funcionario("Carlos", 3500)

f1.aplicar_bonus()
f2.aplicar_bonus()

print(f"Funcionário: {f1.nome}, Salário com bônus: R${f1.salario:.2f}")
print(f"Funcionário: {f2.nome}, Salário com bônus: R${f2.salario:.2f}")