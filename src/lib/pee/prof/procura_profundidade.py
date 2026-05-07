from ..mec_proc.mecanismo_procura import MecanismoProcura
from .fronteira_lifo import FronteiraLIFO

"""
A classe ProcuraProfundidade explora o nó mais fundo possível num único ramo da árvore antes de recuar, utilizando para isso a 
FronteiraLIFO. 
A sua grande vantagem é gastar muito pouca memória ,tem complexidade espacial linear. 
O seu grande problema, no entanto, é que pode nunca encontrar a solução se ficar presa num ramo infinito.
"""

class ProcuraProfundidade(MecanismoProcura):

    def __init__(self):
        super().__init__(FronteiraLIFO())