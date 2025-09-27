"""4. Hierarquia de Classes e Dicionários: Crie uma hierarquia de classes para um sistema
de controle de estoque. Comece com uma classe Produto com atributos como nome e
preco. Em seguida, crie classes filhas como Eletronico e Roupa. A classe Estoque deve
usar um dicionário para armazenar os produtos, onde a chave é o nome do produto e o
valor é o objeto do produto."""


class Produto:
  def __init__(self, nome, preco):
    self.nome = nome
    self.preco = preco

  def __str__(self):
    return f"{self.nome} - R${self.preco:.2f}"

class Eletronico(Produto):
  def __init__(self, nome, preco, quantidade):
    super().__init__(nome, preco)
    self.quantidade = quantidade

class Roupa(Produto):
  def __init__(self, nome, preco, quantidade):
    super().__init__(nome, preco)
    self.quantidade = quantidade

class Estoque:
  def __init__(self):
    self.estoque = {}

  def adicionar_produto(self, produto):
    self.estoque[produto.nome] = produto

  def remover_produto(self, nome):
    if nome in self.estoque:
      del self.estoque[nome]

  def buscar_produto(self, nome):
    return self.estoque.get(nome)

  def listar_produtos(self):
    for produto in self.estoque.values():
      print(f"{produto.nome} - R${produto.preco} - Quantidade: {produto.quantidade}")

tv = Eletronico("TV", 1500, 10)
print(tv)
notebook = Eletronico("Notebook", 4500.00, 3)
celular = Eletronico("Celular", 1800.00, 10)

camisa = Roupa("Camisa", 80.00, 20)
calca = Roupa("Calça Jeans", 120.00, 15)
tenis = Roupa("Tênis", 250.00, 8)

estoque = Estoque()


estoque.adicionar_produto(tv)
estoque.adicionar_produto(notebook)
estoque.adicionar_produto(celular)
estoque.adicionar_produto(camisa)
estoque.adicionar_produto(calca)
estoque.adicionar_produto(tenis)

estoque.listar_produtos()