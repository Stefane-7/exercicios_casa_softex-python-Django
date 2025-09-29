"""1. Herança e Listas: Crie uma classe Animal com um atributo nome e um método
fazer_som(). Crie uma classe Gato que herda de Animal e uma classe Cachorro que
herda de Animal. Crie uma lista que contenha um objeto de cada classe (Gato e
Cachorro) e itere sobre ela para chamar o método fazer_som()."""

class Animal:
  def __init__(self, nome):
    self.nome = nome
  
  def fazer_som(self):
    pass
  
class Gato(Animal):
  def __init__(self, nome):
    super().__init__(nome)
  
  def fazer_som(self):
    print("Miau!")
    
class Cachorro(Animal):
  def __init__(self, nome):
    super().__init__(nome)
  
  def fazer_som(self):
    print("Au! Au!")
    
gato = Gato("Tigrinho")
cachorro = Cachorro("Betovem")

animais = [gato, cachorro]

for animal in animais:
  animal.fazer_som()