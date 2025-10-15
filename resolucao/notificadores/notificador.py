from abc import ABC, abstractmethod
from modelos.pedido import Pedido


class Notificador(ABC):
    @abstractmethod
    def notificar(self, pedido: Pedido):
        pass
