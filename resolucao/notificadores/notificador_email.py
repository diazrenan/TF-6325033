from notificadores.notificador import Notificador


class NotificadorEmail(Notificador):
    def notificar(self, pedido):
        print(f"Enviando e-mail de confirmação para {pedido.cliente_email}...")
