from abc import ABC, abstractmethod
from modelos.pedido import Pedido


class MetodoDePagamento(ABC):
    @abstractmethod
    def pagar(self, pedido: Pedido):
        pass
