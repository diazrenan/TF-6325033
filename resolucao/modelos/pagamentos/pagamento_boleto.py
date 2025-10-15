from pagamentos.metodo_de_pagamento import MetodoDePagamento


class PagamentoBoleto(MetodoDePagamento):
    def pagar(self, pedido):
        print(f"Gerando boleto no valor de R$ {pedido.valor:.2f}...")
