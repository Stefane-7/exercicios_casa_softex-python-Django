"""23. Autenticador de Usuário: Crie uma função autenticar(usuario, senha) que verifica se o
usuário e a senha existem em um dicionário pré-definido. """


usuarios = {
    "joao": "1234",
    "maria": "abcd",
    "pedro": "senha123"
}

def autenticar(usuario: str, senha: str) -> bool:
    if usuario in usuarios:
        return usuarios[usuario] == senha
    return False


while True:
    usuario_entrada = input("Digite seu usuário: ").lower()
    senha_entrada = input("Digite sua senha: ")
    
    if autenticar(usuario_entrada, senha_entrada):
        print("Login realizado com sucesso!")
        break  
    else:
        print("Usuário ou senha incorretos. Tente novamente.")