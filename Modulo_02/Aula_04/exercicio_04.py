"""4. Verificador de Número Par: Crie uma função que receba um número e retorne True se
ele for par e False se for ímpar."""

def Verificador_de_pares(n1: int) -> bool:
  if n1 % 2 == 0:
    return True
  else:
    return False
    
print(Verificador_de_pares(10))
print(Verificador_de_pares(5))
  
  