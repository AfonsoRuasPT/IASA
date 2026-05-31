from ..mec_proc.mecanismo_procura import MecanismoProcura
from .fronteira_lifo import FronteiraLIFO
 
'''
A Procura em Profundidade explora sempre o ramo mais profundo antes de recuar. 
A FronteiraLIFO garante que os nós mais recentes (mais profundos) são sempre os próximos a ser expandidos.
'''
 
class ProcuraProfundidade(MecanismoProcura): # herda de MecanismoProcura; usa FronteiraLIFO para exploração em profundidade
 
    '''
    ProcuraProfundidade configura o mecanismo de procura com FronteiraLIFO, implementando a estratégia de explorar primeiro os nós mais recentes
    (maior profundidade). Não mantém memória de estados explorados, pelo que pode entrar em ciclos infinitos em grafos com ciclos.
 
    ProcuraProfundidade herda de MecanismoProcura.
    '''
 
    """
    A classe ProcuraProfundidade explora o nó mais fundo possível num único ramo da árvore antes de recuar, utilizando para isso a 
    FronteiraLIFO. 
    A sua grande vantagem é gastar muito pouca memória ,tem complexidade espacial linear. 
    O seu grande problema, no entanto, é que pode nunca encontrar a solução se ficar presa num ramo infinito.
    """
 
    def __init__(self):
        super().__init__(FronteiraLIFO()) # inicializa MecanismoProcura com FronteiraLIFO, nós mais recentes são expandidos primeiro

        