from lib.mod.operador import Operador
from ..estado_contagem.estado_contagem import EstadoContagem

class OperadorIncremento(Operador):

    """
    O OperadorIncremento é a implementacao concreta do operador para o problema de contagem.
    Representa a ação de incrementar a contagem atual por um valor especifico.
    Especializamos os metodos abstrados aplicar e custo aplicado ao contexto do problema de contagem.
    """

    def __init__(self, incremento):
        self.__incremento = incremento

    @property
    def incremento(self):
        return self.__incremento
    
    def aplicar(self, estado): 
        # no ambito do nosso problema de contagem aplicar um operador significa incrementar a contagem logo 
        # é so somar o operador ao valor da contagem do estado atual
        return EstadoContagem(estado.contagem + self.__incremento)
    
    def custo(self, estado, estado_sucessor):
        return (self.__incremento)**2
    # o custo do operador é o quadrado do incremento como mencionado no enunciado

