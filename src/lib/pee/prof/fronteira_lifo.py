from ..mec_proc.fronteira import Fronteira
 
'''
A Procura em Profundidade Depth-First Search explora os nós mais recentes primeiro, aprofundando um ramo antes de recuar.
Tem complexidade espacial linear O(bm) e usa muito menos memória que a Procura em Largura -no entanto pode não encontrar solução e pode não ser óptima.
'''
 
class FronteiraLIFO(Fronteira): # herda de Fronteira
 
    '''
    FronteiraLIFO insere novos nós no início da lista (posição 0), criando comportamento LIFO: o nó mais recente (inserido por último) é sempre
    o próximo a ser expandido via remover()/pop(0).
    É a fronteira base da Procura em Profundidade.
    '''
 
    """
    A classe FronteiraLIFO insere os novos nós sempre no início da lista (na posição 0). 
    Isto gera um comportamento "last in first out" (LIFO) , o que significa que o algoritmo vai pegar sempre nos nós mais recentes que acabou de gerar. 
    É a mecanismo principal necessária para pôr a Procura em Profundidade a funcionar.
    """
 
    def inserir(self, no): # insere o nó no início da lista: o nó mais recente fica na posição 0 e é o próximo a ser expandido (LIFO)
        self._nos.insert(0, no) # insere o no na posicao 0