class Pedido:
    def __init__(self, id, valor, cliente_email):
        self.id = id
        self.valor = valor
        self.cliente_email = cliente_email
        self.status = "pendente"

    def concluir(self):
        self.status = "concluido"
