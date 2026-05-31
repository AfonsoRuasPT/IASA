from ..mec_proc.fronteira import Fronteira
 
'''
A Procura em Largura Breadth-First Search explora os nós mais antigos primeiro, nível a nível. 
É óptima e completa, mas tem complexidade espacial exponencial O(bᵈ) / pode necessitar de muita memória.
'''
 
class FronteiraFIFO(Fronteira): # herda de Fronteira
 
    '''
    FronteiraFIFO insere novos nós no final da lista (append), criando comportamento FIFO: o nó mais antigo (inserido primeiro) é sempre
    o próximo a ser expandido via remover()/pop(0).
    É a fronteira base da Procura em Largura.
    '''
 
    """
    A classe FronteiraFIFO gere a fila de espera inserindo os novos nós no final da lista (append). 
    Isto cria a lógica "first in first out" (FIFO), que força o algoritmo a explorar os nós mais antigos primeiro. 
    É esta mecânica exata que serve de base para implementar a Procura em Largura, garantindo que o espaço de estados é explorado 
    nível a nível de forma exaustiva.
    """
 
    def inserir(self, no): # insere o nó no final da lista: o nó mais recente fica no fim e é o último a ser expandido (FIFO)
        self._nos.append(no)