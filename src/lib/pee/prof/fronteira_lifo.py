from ..mec_proc.fronteira import Fronteira

"""
A classe FronteiraLIFO insere os novos nós sempre no início da lista (na posição 0). 
Isto gera um comportamento "last in first out" (LIFO) , o que significa que o algoritmo vai pegar sempre nos nós mais recentes que 
acabou de gerar. 
É a mecanismo principal necessária para pôr a Procura em Profundidade a funcionar.
"""

class FronteiraLIFO(Fronteira):

    def inserir(self, no):
        self._nos.insert(0, no)