from modelos.pedido import Pedido
from pagamentos.metodo_de_pagamento import MetodoDePagamento
from notificadores.notificador import Notificador


class ProcessadorDePedidos:
    def __init__(self, metodo_pagamento: MetodoDePagamento, notificador: Notificador):
        self.metodo_pagamento = metodo_pagamento
        self.notificador = notificador

    def processar(self, pedido: Pedido):
        print(
            f"Processando o pedido #{pedido.id} no valor de R$ {pedido.valor:.2f}...")
        self.metodo_pagamento.pagar(pedido)
        self.notificador.notificar(pedido)
        pedido.concluir()
        print("Pedido concluído!")
