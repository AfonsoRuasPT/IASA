from ..mec_proc.procura_grafo import ProcuraGrafo
from .fronteira_fifo import FronteiraFIFO

"""
A classe ProcuraLargura junta as peças para fazer uma procura nível a nível usando a FronteiraFIFO. 
Este método de procura explora sempre focando-se na menor profundidade. 
Apesar de ser um método de procura completo e ótimo ,garante que encontra a solução e que essa é a melhor possível, 
tem a desvantagem de consumir muita memória, visto que a complexidade espacial cresce de forma exponencial à medida que a árvore alarga.
"""

class ProcuraLargura(ProcuraGrafo):

    def __init__(self):
        super().__init__(FronteiraFIFO())