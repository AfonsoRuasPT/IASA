from pee.melhor_prim.heuristica import Heuristica
import math

'''
A heurística é uma função h que estima o custo até ao estado objectivo. 
A distância euclidiana é uma heurística utilizada para este problema.
'''

class HeurDist(Heuristica): # herda de Heuristica, implementa a função h com base na distância euclidiana

    '''
    HeurDist implementa a heurística de distância euclidiana.
    Estima o custo do estado actual até ao estado final (objectivo) calculando a distância em linha recta entre as duas posições.
    É admissível porque a distância euclidiana nunca sobrestima o custo real do percurso.

    HeurDist herda de Heuristica.
    HeurDist tem uma associação com Estado 
    '''

    def __init__(self, estado_final): # recebe o estado objectivo para calcular a distância em h()
        self.__estado_final = estado_final 

    def h(self, estado): # função heurística que estima o custo de 'estado' até ao estado final
        return math.dist(estado.posicao, self.__estado_final.posicao)
        # calcula a distância euclidiana entre a posição do estado actual e a posição do estado final
        # usada pela ProcuraAA para guiar a procura em direcção ao objectivo de forma informada