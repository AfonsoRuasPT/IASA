from ..mec_proc.fronteira import Fronteira
from heapq import heappush, heappop
 
class FronteiraPrioridade(Fronteira): # herda de Fronteira
 
    '''
    FronteiraPrioridade ordena os nós por prioridade usando a biblioteca
    heapq, heappush insere mantendo a heap, heappop remove sempre o nó com menor prioridade (f(n) mínimo).
    A prioridade de cada nó é calculada pelo Avaliador antes de inserir.
 
    FronteiraPrioridade herda de Fronteira.
    FronteiraPrioridade compõe Avaliador: recebe-o no construtor e usa-o em inserir().
    É usada por ProcuraMelhorPrim.
    '''
 
    """
    A classe FronteiraPrioridade ordena a fila dos nós consoante a prioridade de cada nó, já não utiliza o FIFO e o LIFO, 
    sendo a base da Procura Melhor-Primeiro. 
    Quando um nó é inserido, a classe define a prioridade de cada nó através de um avaliador. 
    Esta fronteira usa a blbioteca heapq para garantir que a fila está sempre ordenada pelo menor valor numérico. 
    Desta forma, na hora de remover, o algoritmo puxa sempre a melhor opção disponível no momento.
    """
 
    def __init__(self, avaliador): # recebe o Avaliador que define o critério de prioridade (custo / heurística)
        super().__init__() # inicia a fronteira
        self.__avaliador = avaliador # Avaliador concreto
 
    def inserir(self, no): # calcula a prioridade do nó e insere-o na heap mantendo a ordenação
        no.prioridade = self.__avaliador.prioridade(no) # define a prioridade do nó usando o avaliador
        heappush(self._nos, no) # insere na heap que mantém _nos ordenada por prioridade crescente
 
    def remover(self): # remove e retorna sempre o nó com menor prioridade
        return heappop(self._nos) # remove da heap, retorna o elemento mínimo