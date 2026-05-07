from pee.melhor_prim.heuristica import Heuristica


class HeuristicaDeContagem(Heuristica):

    def __init__(self, valor_final):
        self.__valor_final = valor_final
    
    def h(self, estado):
        return abs(self.__valor_final - estado.contagem)