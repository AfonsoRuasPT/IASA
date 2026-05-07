from abc import ABC, abstractmethod

class Comportamento(ABC):

    
    """
        Interface que activa a funcionalidade geral de um comportamento.  
     """

    @abstractmethod
    def activar(self, percepcao):
        """Activar o comportamento com base na percepção. Falta implementar o método activar da Interface Comportamento"""


    """
    Interface/Módulo base que define a funcionalidade geral de um comportamento[cite: 201].
    
    Um comportamento é um módulo comportamental que relaciona padrões de perceção 
    com padrões de ação. Consiste num conjunto de reações relacionadas 
    entre si com o intuito de produzir um resultado específico (ex: evitar obstáculos).
    """