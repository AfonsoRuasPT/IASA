from abc import ABC, abstractmethod

class Estimulo(ABC):

    # Define informação activadora de uma reacção

    @abstractmethod
    def detectar(self, percepcao): # retorna uma accao
        """"""