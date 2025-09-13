"""8. Verificador de Login: Crie uma função que receba um nome de usuário e uma senha. Se
o nome for "admin" e a senha for "12345", retorne "Acesso concedido". Caso contrário,
retorne "Acesso negado". Use tipagem para os parâmetros e o retorno."""

def verificar_login(usuario: str, senha: str) -> str:
    if usuario == "admin" and senha == "12345":
        return "Acesso concedido"
    else:
        return "Acesso negado"

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

 
resultado = verificar_login(usuario, senha)
print(resultado)