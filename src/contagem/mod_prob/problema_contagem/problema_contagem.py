from lib.mod.problema import Problema
from ..estado_contagem.estado_contagem import EstadoContagem
from ..operador_incremento.operador_incremento import OperadorIncremento

class ProblemaContagem(Problema):

    """
    O problema de contagem é a implementacao concreta do problema para o contexto da contagem.

    """

    def __init__(self, valor_inicial, valor_final, incrementos):
        """
        Chamamos o construtor da superclasse Problema, passandolhe o estado inicial que é o valor_inicial, e a lista de operadores, OperadorIncremento.

        """
        super().__init__(EstadoContagem(valor_inicial), [OperadorIncremento(inc) for inc in incrementos])
        self.__valor_final = valor_final

    def objectivo(self, estado):
        """
        O objetivo do problema é defenido como atingir ou superar o valor final, ou seja o estado é 
        objetivo se a contagem atual for maior ou igual ao valor final.        
        """
        return estado.contagem >= self.__valor_final