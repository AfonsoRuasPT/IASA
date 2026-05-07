from ..mec_proc.fronteira import Fronteira

"""
A classe FronteiraFIFO gere a fila de espera inserindo os novos nós no final da lista (append). 
Isto cria a lógica "first in first out" (FIFO), que força o algoritmo a explorar os nós mais antigos primeiro. 
É esta mecânica exata que serve de base para implementar a Procura em Largura, garantindo que o espaço de estados é explorado 
nível a nível de forma exaustiva.
"""

class FronteiraFIFO(Fronteira):

    def inserir(self, no):
        self._nos.append(no)