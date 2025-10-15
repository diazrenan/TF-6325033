from pagamentos.metodo_de_pagamento import MetodoDePagamento


class PagamentoCartaoCredito(MetodoDePagamento):
    def pagar(self, pedido):
        print(f"Pagando R$ {pedido.valor:.2f} com cartão de crédito...")
