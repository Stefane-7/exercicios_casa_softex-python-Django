class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.__email = email   

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, novo_email):
        if "@" in novo_email:
            self.__email = novo_email
        else:
            print("❌ ERRO: Email inválido! O email precisa conter '@'.")

class CanalEnvio:
    def enviar(self, mensagem):
        raise NotImplementedError("Você deve sobrescrever o método enviar()!")

class Email(CanalEnvio):
    def enviar(self, mensagem):
        print(f"📧 Enviando para servidor de email: {mensagem}")


class SMS(CanalEnvio):
    def enviar(self, mensagem):
        print(f"📱 Enviando para operadora telefônica: {mensagem}")

class SistemaAlerta:
    def __init__(self, usuario, canal):
        self.usuario = usuario
        self.canal = canal

    def disparar(self, texto):
        mensagem_formatada = f"{self.usuario.nome}, {texto}"
        self.canal.enviar(mensagem_formatada)


if __name__ == "__main__":

    print("\n=== 1. Teste de Segurança do Email ===")
    usuario1 = Usuario("Stefane", "teste@exemplo.com")

    usuario1.email = "email_invalido"   
    usuario1.email = "novoemail@empresa.com"  

    print("\n=== 2. Teste usando Canal Email ===")
    canal_email = Email()
    sistema1 = SistemaAlerta(usuario1, canal_email)
    sistema1.disparar("seu relatório está pronto!")

    print("\n=== 3. Teste Polimorfismo com SMS ===")
    canal_sms = SMS()
    sistema2 = SistemaAlerta(usuario1, canal_sms)
    sistema2.disparar("alerta crítico: servidor caiu!")
