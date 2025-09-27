"""3. Polimorfismo e Tuplas: Crie uma classe Conta com um método obter_saldo(). Crie uma
classe filha ContaPoupanca que sobrescreve o método obter_saldo() para retornar o
saldo e a taxa de juros como uma tupla (saldo, juros)."""

# Classe base Conta
class Conta:
    def __init__(self, saldo):
        self.saldo = saldo
    
    def obter_saldo(self):
        # Método que retorna apenas o saldo
        return self.saldo


# Classe filha ContaPoupanca
class ContaPoupanca(Conta):
    def __init__(self, saldo, juros):
        # Reaproveita o saldo da classe pai e adiciona juros
        super().__init__(saldo)
        self.juros = juros
    
    def obter_saldo(self):
        # Retorna saldo e juros como uma tupla
        return (self.saldo, self.juros)


# --- Testando ---
conta_normal = Conta(1000)
print("Conta comum ->", conta_normal.obter_saldo())  
# Saída: 1000

conta_poupanca = ContaPoupanca(2000, 0.05)
print("Conta poupança ->", conta_poupanca.obter_saldo())  
# Saída: (2000, 0.05)