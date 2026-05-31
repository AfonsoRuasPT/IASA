from ..mec_proc.procura_grafo import ProcuraGrafo
from .fronteira_prioridade import FronteiraPrioridade

class ProcuraMelhorPrim(ProcuraGrafo):

    '''
    Herda de ProcuraGrafo (evita ciclos) e substitui a fronteira por uma FronteiraPrioridade. 
    Reescreve o metodo _manter() para também manter também nós com um custo mais baixo.
 
    ProcuraMelhorPrim herda de ProcuraGrafo.
    '''

    """
    A classe ProcuraMelhorPrim é o motor genérico das procuras que não escolhem os nós apenas pela ordem de chegada, mas sim por 
    uma função de avaliação. 
    Herda da ProcuraGrafo para continuar a evitar ciclos infinitos, mas ao iniciar, substitui a fila de espera normal por uma 
    FronteiraPrioridade, entregando-lhe o avaliador escolhido. 
    O método _manter reescrito: um nó entra na memória não apenas se for um estado totalmente novo (verificado pelo 
    super()._manter(no)), mas também se for um estado já visitado onde acabámos de descobrir um atalho mais barato 
    (no.custo < self._explorados[no.estado].custo). 
    É isto que garante que o algoritmo corrige a sua rota se arranjar uma forma melhor de chegar ao mesmo ponto.
    """

    def __init__(self, avaliador):
        super().__init__(FronteiraPrioridade(avaliador)) # inicializa ProcuraGrafo com FronteiraPrioridade
        self._avaliador = avaliador # guarda o avaliador


    def _manter(self, no): 
        return super()._manter(no) or no.custo < self._explorados[no.estado].custo 
    # o nó tambem se mantem se o custo desse nó for inferior ao custo do nó na lista explorados