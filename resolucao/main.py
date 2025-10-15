from modelos.pedido import Pedido
from pagamentos.pagamento_cartao_credito import PagamentoCartaoCredito
from pagamentos.pagamento_boleto import PagamentoBoleto
from pagamentos.pagamento_pix import PagamentoPix
from notificadores.notificador_email import NotificadorEmail
from notificadores.notificador_sms import NotificadorSMS
from processador.processador_de_pedidos import ProcessadorDePedidos

if __name__ == "__main__":
    pedido1 = Pedido(123, 150.75, "cliente@exemplo.com")
    processador1 = ProcessadorDePedidos(
        PagamentoCartaoCredito(), NotificadorEmail())
    processador1.processar(pedido1)

    print("-" * 20)

    pedido2 = Pedido(456, 200.00, "cliente2@exemplo.com")
    processador2 = ProcessadorDePedidos(PagamentoBoleto(), NotificadorEmail())
    processador2.processar(pedido2)

    print("-" * 20)

    pedido3 = Pedido(789, 350.00, "cliente3@exemplo.com")
    processador3 = ProcessadorDePedidos(PagamentoPix(), NotificadorSMS())
    processador3.processar(pedido3)
