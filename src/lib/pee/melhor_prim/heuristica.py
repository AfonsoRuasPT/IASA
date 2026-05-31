from abc import ABC, abstractmethod

class Heuristica(ABC):

    '''
    Heuristica define o contrato da função h(n).
    h(n) representa uma estimativa do custo desde o estado n até ao objectivo.
    '''

    """
    A classe Heuristica é uma class abstrata para injetar inteligência no algoritmo. 
    O seu único método, h, é abstrato e obriga qualquer classe que a herde a definir uma forma matemática de 
    calcular a estimativa do custo entre um determinado estado e o estado objetivo. 
    É isto que permite que as procuras informadas não andem "às cegas", dando-lhes um palpite educado sobre a distância que falta 
    percorrer para saberem que caminhos priorizar.
    """

    @abstractmethod
    def h(self, estado):  # segundo o estado esta função devolve a estimativa do custo até ao objectivo
        """"""