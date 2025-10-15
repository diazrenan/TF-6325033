from pagamentos.metodo_de_pagamento import MetodoDePagamento


class PagamentoPix(MetodoDePagamento):
    def pagar(self, pedido):
        print(f"Pagando R$ {pedido.valor:.2f} via PIX...")
