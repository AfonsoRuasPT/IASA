from pee.melhor_prim.heuristica import Heuristica
import math
class HeurDist(Heuristica):

    def __init__(self, estado_final):
        self.__estado_final = estado_final

    def h(self, estado):
        return math.dist(estado.posicao, self.__estado_final.posicao)
        
