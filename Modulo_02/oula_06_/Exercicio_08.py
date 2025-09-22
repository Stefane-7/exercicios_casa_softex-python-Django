"""Exercício 8: Um Carro que Anda
Crie uma classe Carro com os atributos modelo e nivel_combustivel (começando com 0).
1. Crie um método para abastecer(litros) que aumenta o nível de combustível.
2. Crie um método dirigir(distância) que consome combustível (ex: 1 litro a cada 10 km). O
método deve verificar se há combustível suficiente para a viagem. Se houver, diminua o
combustível e avise que o carro andou. Se não, avise que não há combustível."""


class Carro:
  def __init__(self, modelo: str, nivel_combustivel: float) -> None:
    self.modelo = modelo
    self.nivel_combustivel = nivel_combustivel
    
  def abastecer(self, valor: float):
    if valor > 0:
      self.nivel_combustivel = valor