class Mensagem:
    def __init__(self, texto, data_envio, arquivo, formato, duracao):
        self.texto = texto
        self.data_envio = data_envio
        self.arquivo = arquivo
        self.formato = formato
        self.duracao = duracao

class Canal:
    def __init__(self, numero_telefone, nome_usuario):
        self.numero_telefone = numero_telefone
        self.nome_usuario = nome_usuario

def main():
    # Criando instâncias das classes com os valores especificados
    mensagem_exemplo = Mensagem("bom dia!", "04/12", ".msg", "jpg", "2 min")
    canal_exemplo = Canal("+55 11 987654321", "Jose R.")

    # Solicitando a escolha do usuário
    escolha_canal = int(input("Escolha um canal: 1 - Telegram/WhatsApp, 2 - Facebook/Instagram: "))

    if escolha_canal == 1:
        escolha_mensagem = int(input("Escolha uma mensagem: 1-texto, 2-vídeo, 3-foto, 4-arquivo: "))

        if escolha_mensagem == 1:
            
            print(f"Mensagem enviada à: {canal_exemplo.numero_telefone}. \nDados da mensagem: Texto: {mensagem_exemplo.texto}, Data de Envio: {mensagem_exemplo.data_envio}")
        elif escolha_mensagem == 2:
            
            print(f"Mensagem enviada à: {canal_exemplo.numero_telefone}. \nData de Envio: {mensagem_exemplo.data_envio}, Arquivo: {mensagem_exemplo.arquivo}, Formato: {mensagem_exemplo.formato}, Duração: {mensagem_exemplo.duracao}")
        elif escolha_mensagem == 3 or escolha_mensagem == 4:
            
            print(f"Mensagem enviada à: {canal_exemplo.numero_telefone}. \nData de Envio: {mensagem_exemplo.data_envio}, Arquivo: {mensagem_exemplo.arquivo}, Formato: {mensagem_exemplo.formato}")
        else:
            print("Escolha inválida.")

    elif escolha_canal == 2:
        escolha_mensagem = int(input("Escolha uma mensagem: 1-texto, 2-vídeo, 3-foto, 4-arquivo: "))

        if escolha_mensagem == 1:
            
            print(f"Mensagem enviada à: {canal_exemplo.nome_usuario}. \nDados da mensagem: Texto: {mensagem_exemplo.texto}, Data de Envio: {mensagem_exemplo.data_envio}")
        elif escolha_mensagem == 2:
            
            print(f"Mensagem enviada à: {canal_exemplo.nome_usuario}. \nData de Envio: {mensagem_exemplo.data_envio}, Arquivo: {mensagem_exemplo.arquivo}, Formato: {mensagem_exemplo.formato}, Duração: {mensagem_exemplo.duracao}")
        elif escolha_mensagem == 3 or escolha_mensagem == 4:
            
            print(f"Mensagem enviada à: {canal_exemplo.nome_usuario}. \nData de Envio: {mensagem_exemplo.data_envio}, Arquivo: {mensagem_exemplo.arquivo}, Formato: {mensagem_exemplo.formato}")
        else:
            print("Escolha inválida.")
    else:
        print("Escolha inválida.")

if __name__ == "__main__":
    main()