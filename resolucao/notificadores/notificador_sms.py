from notificadores.notificador import Notificador


class NotificadorSMS(Notificador):
    def notificar(self, pedido):
        print(f"Enviando SMS de confirmação para {pedido.cliente_email}...")
