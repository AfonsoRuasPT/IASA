from ..mec_proc.fronteira import Fronteira
from heapq import heappush, heappop

class FronteiraPrioridade(Fronteira):


    """
    A classe FronteiraPrioridade ordena a fina dos nós consoante a prioridade de cada nó, já não utiliza o FIFO e o LIFO, 
    sendo a base da Procura Melhor-Primeiro. 
    Quando um nó é inserido, a classe define a prioridade de cada nó através de um avaliador. 
    Esta fronteira usa a blbioteca heapq para garantir que a fila está sempre ordenada pelo menor valor numérico. 
    Desta forma, na hora de remover, o algoritmo puxa sempre a melhor opção disponível no momento.
    """

    def __init__(self, avaliador):
        super().__init__()
        self.__avaliador = avaliador

    def inserir(self, no):
        no.prioridade = self.__avaliador.prioridade(no)
        heappush(self._nos, no) # faltava o _ no self._nos, porque nos é defenido como protected na class mae

    def remover(self):
        return heappop(self._nos) # faltava o _ no self._nos, porque nos é defenido como protected na class mae