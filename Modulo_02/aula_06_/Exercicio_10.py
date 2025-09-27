"""Exercício 10: Um Objeto Dentro de Outro
Crie duas classes: Motor e Carro.
1. A classe Motor terá um atributo potencial.
2. A classe Carro terá modelo. Ao criar um Carro, ele deve também criar um objeto Motor e
guardá-lo como um de seus atributos (ex: self.motor = Motor(100)).
Crie um método no Carro chamado exibir_potencia que imprime a potência do seu motor."""


class Carro:

    def __init__(self, modelo: str):

        self.modelo = modelo
        self.nivel_combustivel = 0.0

    def __str__(self):

        return f"{self.modelo} — Combustível: {self.nivel_combustivel:.2f} L"

    def abastecer(self, litros: float) -> None:
        """
        Aumenta o nível de combustível.
        Só aceita valores positivos.
        """
        if litros <= 0:
            print("Erro: informe um valor de litros maior que zero.")
            return
        self.nivel_combustivel += litros
        print(f"{self.modelo}: Abastecido com {litros:.2f} L. Nível atual: {self.nivel_combustivel:.2f} L")

    def dirigir(self, distancia: float) -> None:
        
        if distancia <= 0:
            print("Erro: informe uma distância positiva.")
            return

        consumo_por_km = 0.1  
        litros_necessarios = distancia * consumo_por_km

        if self.nivel_combustivel >= litros_necessarios:
            self.nivel_combustivel -= litros_necessarios
            print(f"{self.modelo} andou {distancia} km e consumiu {litros_necessarios:.2f} L. "
                  f"Combustível restante: {self.nivel_combustivel:.2f} L.")
        else:
            km_possiveis = self.nivel_combustivel / consumo_por_km if consumo_por_km > 0 else 0
            print(f"Não há combustível suficiente para {distancia} km. "
                  f"Com {self.nivel_combustivel:.2f} L dá para andar {km_possiveis:.1f} km.")


carro = Carro("Fusca")
print(carro)                 
carro.abastecer(5)           
carro.dirigir(30)      
carro.dirigir(25)        
carro.abastecer(2.5)         
carro.dirigir(25)    
print(carro)   