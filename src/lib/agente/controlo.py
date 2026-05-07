from abc import ABC, abstractmethod


class Controlo(ABC): # classe abstrata Controlo, que define a interface para o controlo do agente

    @abstractmethod
    def processar(self, percepcao):
        """Processar a percepção e retornar uma acção. Falta implementar o método processar da Interface Controlo"""